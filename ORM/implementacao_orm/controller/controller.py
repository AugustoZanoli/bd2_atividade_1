from implementacao_orm.dao.dao import DAO
from implementacao_orm.view.view import View

class Controller:
    def __init__(self, dao: DAO):
        self.dao = dao

    def create_order(self, customer_name, employee_name, order_date, order_details):
        self.dao.add_order(customer_name, employee_name, order_date, order_details)

    def view_order(self, order_id):
        self.dao.get_order_by_id(order_id)

    def view_employee_ranking(self, start_date, end_date):
        ranking = self.dao.get_employee_ranking(start_date, end_date)
        View().mostrar_ranking(ranking)