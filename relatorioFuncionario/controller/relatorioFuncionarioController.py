from relatorioFuncionario.dao.relatorioFuncionarioDao import RankingFuncionarioDAO
from relatorioFuncionario.view.relatorioFuncionarioView import formRanking, mostrarRanking

def executarRanking():
    data_inicio, data_fim = formRanking()
    dao = RankingFuncionarioDAO()
    ranking = dao.buscarRanking(data_inicio, data_fim)
    mostrarRanking(ranking)
