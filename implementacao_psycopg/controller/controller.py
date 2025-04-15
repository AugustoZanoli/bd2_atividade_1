from implementacao_psycopg.dao.dao import PedidoDAO
from implementacao_psycopg.view.view import formsInserir

def executarInsercao():
    nomeCliente, nomeVendedor, dataPedido, itens = formsInserir()
    dao = PedidoDAO()
    dao.inserirPedido(nomeCliente, nomeVendedor, dataPedido, itens)
