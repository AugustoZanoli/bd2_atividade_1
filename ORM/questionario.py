from implementacao_orm.controller.controller import Controller
from implementacao_orm.dao.dao import DAO
from implementacao_orm.view.view import View
from implementacao_orm.db.connect import connect 

def questionario():
    engine = connect()
    dao = DAO(engine)
    controller = Controller(dao)
    view = View()

    print("\nSelecione uma opção:")
    print("1 - Inserir pedido")
    print("2 - Consultar pedido")
    print("3 - Consultar ranking de vendedores")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        customer_name, employee_name, order_date, order_details = view.get_order_details()
        controller.create_order(customer_name, employee_name, order_date, order_details)

    elif opcao == "2":
        order_id = view.get_order_id()
        controller.view_order(order_id)

    elif opcao == "3":
        start_date, end_date = view.get_date_range()
        controller.view_employee_ranking(start_date, end_date)

    elif opcao == "4":
        print("Encerrando o programa.")

    else:
        print("Opção inválida.")