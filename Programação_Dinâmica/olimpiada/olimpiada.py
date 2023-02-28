def soma_de_numeros_menores(valor_da_soma, qtd_operandos):
    qtd_somas = [
        [0 for w in range(qtd_operandos + 1)] for j in range(0, valor_da_soma + 1)
    ]
    qtd_somas[0][0] = 1
    for n in range(1, valor_da_soma + 1):
        for x in range(1, qtd_operandos + 1):
            for k in range(1, min(n, x) + 1):
                # print(
                #     f"[{n if n>=10 else f' {n}'}][{x}] = {qtd_somas[n][x]} += qtd_somas[{n if n>=10 else f' {n}'} - {k}][{x} - 1] = {qtd_somas[n - k][x - 1]}"
                # )
                qtd_somas[n][x] += qtd_somas[n - k][x - 1]
    # for ad in range(0, len(qtd_somas)):
    #     print(qtd_somas[ad])
    return qtd_somas[valor_da_soma][qtd_operandos]


out = []


def main(entrada):
    n = 1
    x = 1

    # entrada = input()
    # [n, x] = map(int, entrada.split())
    # n = 20
    # x = 2

    for i in range(0, len(entrada), 2):
        [n, x] = [entrada[i], entrada[i + 1]]
        out.append(soma_de_numeros_menores(n, x) % 1000000)

        # [n, x] = map(int, entrada.split())
    return out
