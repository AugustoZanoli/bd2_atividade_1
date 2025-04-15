def formBuscarPedido():
    orderId = input("Digite o ID do pedido que deseja buscar: ")
    return int(orderId)

def mostrarPedido(pedido):
    if not pedido:
        print("Pedido não encontrado.")
        return
    
    print(f"\nNúmero do pedido: {pedido['orderid']}")
    print(f"Data do pedido: {pedido['orderdate']}")
    print(f"Nome do cliente: {pedido['cliente']}")
    print(f"Nome do vendedor: {pedido['vendedor']}")
    print("\nItens:")
    for item in pedido["itens"]:
        print(f"- Produto: {item['produto']} - Quantidade: {item['quantidade']} - Preço: R${item['preco']:.2f}")
