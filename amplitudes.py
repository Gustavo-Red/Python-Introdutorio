def amplitudes(dados_semana):
    amplitude = []

    for maximo, minimo in dados_semana:
        amplitude.append(maximo - minimo)

    return amplitude


tuplas = [(34.5, 22.1), (35.0, 23.0), (33.8, 21.5)]
print(amplitudes(tuplas))