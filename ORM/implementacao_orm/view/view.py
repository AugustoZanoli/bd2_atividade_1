from datetime import datetime

class View:
    def get_order_details(self):
        # Pega o nome do cliente e do vendedor
        customer_name = input("Nome do cliente: ")
        employee_name = input("Nome do vendedor: ")

        # Valida a data do pedido até o usuário digitar corretamente
        while True:
            data_pedido_input = input("Data do pedido (YYYY-MM-DD): ")
            try:
                order_date = datetime.strptime(data_pedido_input, "%Y-%m-%d")
                break
            except ValueError:
                print("Data inválida. Use o formato YYYY-MM-DD.")

        # Cria uma lista para armazenar os itens do pedido
        order_details = []
        while True:
            product_id_input = input("ID do produto (ou 'sair' para finalizar): ")
            if product_id_input.lower() == 'sair':
                break

            # Tenta pegar os dados do item corretamente
            try:
                product_id = int(product_id_input)
                unit_price = float(input("Preço unitário: "))
                quantity = int(input("Quantidade: "))
                order_details.append({
                    "product_id": product_id,
                    "unit_price": unit_price,
                    "quantity": quantity
                })
            except ValueError:
                print("Erro nos dados inseridos. Tente novamente.")

        # Retorna todos os dados coletados
        return customer_name, employee_name, order_date, order_details

    def get_order_id(self):
        while True:
            try:
                return int(input("Digite o ID do pedido que deseja buscar: "))
            except ValueError:
                print("ID inválido. Tente novamente.")

    def get_date_range(self):
        while True:
            try:
                start = input("Data inicial (YYYY-MM-DD): ")
                end = input("Data final (YYYY-MM-DD): ")
                start_date = datetime.strptime(start, "%Y-%m-%d")
                end_date = datetime.strptime(end, "%Y-%m-%d")
                return start_date, end_date
            except ValueError:
                print("Formato de data inválido. Use YYYY-MM-DD.")

    def mostrar_ranking(self, ranking):
        if not ranking:
            print("Nenhum resultado encontrado para o intervalo informado.")
            return

        print("\nRANKING DE FUNCIONÁRIOS\n")
        print(f"{'Colocação':10} {'Funcionário':30} {'Pedidos':10} {'Total Vendido':15}\n")

        for index, (funcionario, total_pedidos, total_vendido) in enumerate(ranking, start=1):
            print(f"{index:<10} {funcionario:30} {total_pedidos:<10} R${total_vendido:.2f}")
