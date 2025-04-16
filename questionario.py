from implementacao_psycopg.controller.controller import executarInsercao
from implementacao_psycopg.controller.controller import executarInsercaoInjection
from relatorioPedido.controller.relatorioPedidoController import executarRelatorio
from relatorioFuncionario.controller.relatorioFuncionarioController import executarRanking


def questionario():
        print('Selecione uma opção:')
        print('1 - Inserir pedido')
        print('2 - Consultar pedido')
        print('3 - Consultar ranking de vendedores')
        print('4 - Sair')

        case = int(input())

        if case == 1:
                fluxo()
        elif case == 2:
                executarRelatorio()
        elif case == 3:
                executarRanking()
        else:
                return
        
def fluxo():
        print('Deseja inserir com (1) ou sem (2) injection ?')

        case = int(input())

        if case == 1:
                executarInsercao()
        elif case == 2:
                executarInsercaoInjection()
        else:
                fluxo()