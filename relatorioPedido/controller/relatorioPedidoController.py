from relatorioPedido.dao.relatorioPedidoDao import RelatorioPedidoDAO
from relatorioPedido.view.relatorioPedidoView import formBuscarPedido, mostrarPedido

def executarRelatorio():
    orderId = formBuscarPedido()
    dao = RelatorioPedidoDAO()
    pedido = dao.buscarPedido(orderId)
    mostrarPedido(pedido)
