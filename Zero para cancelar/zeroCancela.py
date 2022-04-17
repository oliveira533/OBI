nNumeros = int(input())
sAux = str(nNumeros)
nValores = list(sAux)
nCont = 0
nLimite = len(nValores)
i = 0
nResultado = 0

while nCont != nLimite:
    if nValores[nCont] == '0' and nValores[(nCont-1)] != '1':
        del(nValores[(nCont-1)])
        del(nValores[(nCont-1)])
        nCont-=2
        nLimite-=2
        
    nCont+=1

del(nValores[0])

while i != len(nValores):
    nResultado = nResultado + int(nValores[i])
    i+=1

print(nResultado)