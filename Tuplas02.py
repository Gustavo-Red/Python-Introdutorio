def resumo_tarefas(tarefas):
    horas_trabalhadas = 0
    horas_pendentes = 0

    for nome, concluida, horas in tarefas:
        if concluida:
            horas_trabalhadas += horas
        else:
            horas_pendentes += horas

    return (horas_trabalhadas, horas_pendentes)


# Teste
tarefas = [("Levantamento de requisitos", True, 8), ("Modelagem do banco", True, 5), ("Desenvolvimento backend", False, 20), ("Testes", False, 10), ("Deploy", False, 3)]

trabalhadas, pendentes = resumo_tarefas(tarefas)
print(f"Horas trabalhadas: {trabalhadas}")
print(f"Horas pendentes:   {pendentes}")


