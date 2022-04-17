nNumeros = int(input()) # peguei o valor uando uminput, mas somente inteiros
sAux = str(nNumeros) # converto os valores inteiros para uma string
nValores = list(sAux) # crio uma lista com os valotes que eu tenho
nCont = 0 # crio um contador
nLimite = len(nValores) # defino uma variável para ser usada como limete do meu contador
i = 0 # variável de contadore
nResultado = 0 # variável utilizada para guardar vaolor final

while nCont != nLimite:
    if nValores[nCont] == '0' and nValores[(nCont-1)] != '1': # testo se o valor é 0 ou 10
        del(nValores[(nCont-1)]) # deleto o valor anterior ao 0
        del(nValores[(nCont-1)]) # deleto o 0
        nCont-=2 # volto o contador 2 números antes para poder recomeçar
        nLimite-=2 # diminuo o limite
        
    nCont+=1

del(nValores[0]) # deleto o primeiro valor, pois ele é ignorado na conta

# bloco de código para fazer a soma de todos os valores da lista
while i != len(nValores):
    nResultado = nResultado + int(nValores[i])
    i+=1

print(nResultado) # exibição de resultado