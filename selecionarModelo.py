from ORM.questionario import questionario as questionarioORM
from implementacao_psycopg.questionario import questionario as questionarioPsyco


def selecionarModelo():
        print('Selecione qual implementação deseja utilizar:')
        print('1 - Psycopg')
        print('2 - ORM SqlAlchemy')

        case = int(input())

        if case == 1:
                questionarioPsyco()
        elif case == 2:
                questionarioORM()
        else:
                print('Opção inválida!')
                selecionarModelo()