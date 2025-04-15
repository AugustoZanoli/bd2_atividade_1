def formsInserir():
    nomeCliente = input("Nome do cliente: ")
    nomeVendedor = input("Nome do vendedor: ")
    dataPedido = input("Data do pedido (YYYY-MM-DD): ")

    itens = []
    while True:
        pid = input("ID do produto (ou 'sair'): ")
        if pid.lower() == "sair":
            break
        precoUnitario = float(input("Preço unitário: "))
        quantity = int(input("Quantidade: "))
        itens.append({
            "productid": int(pid),
            "unitprice": precoUnitario,
            "quantity": quantity
        })

    return nomeCliente, nomeVendedor, dataPedido, itens
