def formulario_insercao():
    nome_cliente = input("Nome do cliente: ")
    nome_vendedor = input("Nome do vendedor: ")
    data_pedido = input("Data do pedido (YYYY-MM-DD): ")

    itens = []
    while True:
        pid = input("ID do produto (ou 'sair'): ")
        if pid.lower() == "sair":
            break
        unit_price = float(input("Preço unitário: "))
        quantity = int(input("Quantidade: "))
        itens.append({
            "productid": int(pid),
            "unitprice": unit_price,
            "quantity": quantity
        })

    return nome_cliente, nome_vendedor, data_pedido, itens
