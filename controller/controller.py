from dao.dao import PedidoDAO
from view.view import formulario_insercao

def executar_insercao():
    nome_cliente, nome_vendedor, data_pedido, itens = formulario_insercao()
    dao = PedidoDAO()
    dao.inserir_pedido(nome_cliente, nome_vendedor, data_pedido, itens)
