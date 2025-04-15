from dao.dao import PedidoDAO
from view.view import formsInserir

def executarInsercao():
    nomeCliente, nomeVendedor, dataPedido, itens = formsInserir()
    dao = PedidoDAO()
    dao.inserirPedido(nomeCliente, nomeVendedor, dataPedido, itens)
