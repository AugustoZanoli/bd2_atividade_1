def formRanking():
    data_inicio = input("Data inicial (YYYY-MM-DD): ")
    data_fim = input("Data final (YYYY-MM-DD): ")
    return data_inicio, data_fim

def mostrarRanking(ranking):
    index = 0
    if not ranking:
        print("Nenhum resultado encontrado para o intervalo informado.")
        return

    # Só imprimindo o ranking de forma bonita, :x e :<y são deslocamentos de casas no print
    print("\nRANKING DE FUNCIONÁRIOS\n")
    print(f"{'Colocação':10} {'Funcionário':30} {'Pedidos':10} {'Total Vendido':15}\n")
    for funcionario, total_pedidos, total_vendido in ranking:
        index = index + 1
        print(f"{index:<10} {funcionario:30} {total_pedidos:<10} R${total_vendido:.2f}")
