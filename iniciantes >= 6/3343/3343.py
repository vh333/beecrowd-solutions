NumT, TamM = map(int, input().split())
sequencia = input()
P, M, G = map(int, input().split())
muralha = [TamM]
ultimas_posicoes = {'P': 0, 'M': 0, 'G': 0}
for i in range(NumT):
    tipo = sequencia[i]
    Tvid = P if tipo == 'P' else M if tipo == 'M' else G
    x = ultimas_posicoes[tipo]
    while Tvid > muralha[x]:
        x += 1
        if len(muralha) == x:
            muralha.append(TamM)
    muralha[x] -= Tvid
    ultimas_posicoes[tipo] = x
print(len(muralha))
