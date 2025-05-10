
def classificacao_final(jogadores):
    import functools

    jogadores.sort(key=functools.cmp_to_key(ordenacao), reverse=True)

    return jogadores


def ordenacao(jogador1, jogador2):
    maior = maior_pontuacao(jogador1, jogador2)
    if maior != 0:
        return maior

    confronto = confronto_direto(jogador1, jogador2)
    if confronto != 0:
        return confronto

    vitoria = numero_vitorias(jogador1, jogador2)
    if vitoria != 0:
        return vitoria

    wo = vitoria_wo(jogador1, jogador2)
    if wo != 0:
        return wo

    return 0


def maior_pontuacao(jogador1, jogador2):
    if jogador1["pontos"] > jogador2["pontos"]:
        return 1
    elif jogador1["pontos"] < jogador2["pontos"]:
        return -1
    else:
        return 0


def confronto_direto(jogador1, jogador2):
    if jogador1["nome"] in jogador2["vitoriascontra"]:
        return -1
    elif jogador2["nome"] in jogador1["vitoriascontra"]:
        return 1
    return 0


def numero_vitorias(jogador1, jogador2):
    if jogador1["vitorias"] > jogador2["vitorias"]:
        return 1
    elif jogador1["vitorias"] < jogador2["vitorias"]:
        return -1
    return 0


def vitoria_wo(jogador1, jogador2):
    if jogador1["vitorias_por_wo"] > jogador2["vitorias_por_wo"]:
        return -1
    elif jogador1["vitorias_por_wo"] < jogador2["vitorias_por_wo"]:
        return 1
    return 0


def calcular_partidas(jogadores, partidas):
    for partida in partidas:
        #encontrar jogadores
        jogador1 = next((j for j in jogadores if j["nome"] == partida["jogador1"]), None)
        jogador2 = next((j for j in jogadores if j["nome"] == partida["jogador2"]), None)

        if not jogador1 or not jogador2:
            raise ValueError(f"Jogadores não encontrados na partida: {partida}")

        #atualizar rodadas
        if partida["resultado"] == "w":  # Vitória do jogador 1
            jogador1["pontos"] += 1
            print(jogador1)
            print(jogadores)
            jogador1["vitorias"] += 1
            jogador1["vitoriascontra"].append(jogador2["nome"])
            if partida["wo"] == "s":
                jogador1["vitorias_por_wo"] += 1

        elif partida["resultado"] == "b":  # Vitória do jogador 2
            jogador2["pontos"] += 1
            jogador2["vitorias"] += 1
            jogador2["vitoriascontra"].append(jogador1["nome"])
            if partida["wo"] == "s":
                jogador2["vitorias_por_wo"] += 1

        elif partida["resultado"] == "d":  # Empate
            jogador1["pontos"] += 0.5
            jogador2["pontos"] += 0.5

    return jogadores


def input_dados():
    partidas = []
    wo = ""
    while True:
        jogador1 = input("Digite o nome do jogador de brancas (ou tecle 'X' para sair): ").lower()
        if jogador1 == "x":
            break

        jogador2 = input("Digite o nome do jogador de pretas: ").lower()
        resultado = input("Resultado (w para brancas, b para pretas, d para empate): ").lower()
        if resultado == "w" or resultado == "b":
            wo = input("Foi WO? (S para sim, N para não): ").lower()

        partidas.append({
            "jogador1": jogador1,
            "jogador2": jogador2,
            "resultado": resultado,
            "wo": wo,
        })

    return partidas


def saida_dados(jogadores):
    print("\nClassificação Final:")
    print("\n--------------------")
    posicao = 1
    for jogador in jogadores:
        print(
            f"{posicao}º - {jogador['nome'].upper()} - {jogador['pontos']} pontos, {jogador['vitorias']} vitórias")
        posicao += 1


def dados_do_sistema():
    jogadores = [
        {"nome": "GABRIEL"},
        {"nome": "PEDRO"},
        {"nome": "JOAO"},
        {"nome": "ANA"},
        {"nome": "MARIA"},
    ]
    for jogador in jogadores:
        jogador["nome"] = jogador["nome"].lower()
        jogador["pontos"] = 0
        jogador["vitorias"] = 0
        jogador["vitoriascontra"] = []
        jogador["vitorias_por_wo"] = 0

    return jogadores


if __name__ == "__main__":
    competidores = dados_do_sistema()
    partidas = input_dados()
    jogadores = calcular_partidas(competidores, partidas)
    classicacao = classificacao_final(jogadores)
    saida_dados(classicacao)