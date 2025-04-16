from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, and_
from implementacao_orm.model.model import Customer, Order, OrderDetail, Employee, Product

class DAO:
    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

    def add_order(self, customer_name, employee_name, order_date, order_details):
        session = self.Session()
        try:
            customer = session.query(Customer).filter(Customer.contact_name == customer_name).first()
            if not customer:
                print(f"Cliente '{customer_name}' não encontrado!")
                return

            employee = session.query(Employee).filter(
                func.concat(Employee.first_name, ' ', Employee.last_name) == employee_name
            ).first()
            if not employee:
                print(f"Vendedor '{employee_name}' não encontrado!")
                return

            for item in order_details:
                product = session.query(Product).filter(Product.product_id == item['product_id']).first()
                if not product:
                    print(f"Produto com ID {item['product_id']} não encontrado!")
                    return

            max_order_id = session.query(func.coalesce(func.max(Order.order_id), 0)).scalar()
            next_order_id = max_order_id + 1

            order = Order(
                order_id=next_order_id,
                customer_id=customer.customer_id,
                employee_id=employee.employee_id,
                order_date=order_date
            )
            session.add(order)

            for item in order_details:
                detail = OrderDetail(
                    order_id=order.order_id,
                    product_id=item['product_id'],
                    unit_price=item['unit_price'],
                    quantity=item['quantity'],
                    discount=item.get('discount', 0)
                )
                session.add(detail)

            session.commit()
            print(f"Pedido criado com sucesso! ID: {order.order_id}")
        except Exception as e:
            session.rollback()
            print("ERRO ao inserir pedido:", e)
        finally:
            session.close()
            print("Sessão encerrada.")

    def get_order_by_id(self, order_id):
        session = self.Session()
        try:
            order = session.query(Order).filter(Order.order_id == order_id).first()
            if not order:
                print(f"Pedido {order_id} não encontrado.")
                return

            customer = order.customer
            employee = order.employee

            print(f"\nNúmero do pedido: {order.order_id}")
            print(f"Data do pedido: {order.order_date}")
            print(f"Nome do cliente: {customer.company_name}")
            print(f"Nome do vendedor: {employee.first_name} {employee.last_name}\n")
            print("Itens:")

            for item in order.order_details:
                print(f"- Produto: {item.product.product_name} - Quantidade: {item.quantity} - Preço: R${item.unit_price:.2f}")
        except Exception as e:
            print("Erro ao consultar pedido:", e)
        finally:
            session.close()

    def get_employee_ranking(self, start_date, end_date):
        session = self.Session()
        try:
            results = (
                session.query(
                    func.concat(Employee.first_name, ' ', Employee.last_name).label("funcionario"),
                    func.count(func.distinct(Order.order_id)).label("total_pedidos"),
                    func.sum(OrderDetail.unit_price * OrderDetail.quantity * (1 - OrderDetail.discount)).label("total_vendido")
                )
                .join(Order, Employee.employee_id == Order.employee_id)
                .join(OrderDetail, Order.order_id == OrderDetail.order_id)
                .filter(and_(Order.order_date >= start_date, Order.order_date <= end_date))
                .group_by("funcionario")
                .order_by(func.sum(OrderDetail.unit_price * OrderDetail.quantity * (1 - OrderDetail.discount)).desc())
                .all()
            )

            return results

        except Exception as e:
            print("Erro ao consultar ranking:", e)
            return []
        finally:
            session.close()