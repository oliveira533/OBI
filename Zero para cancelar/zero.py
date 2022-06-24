nQuantidade = int(input()) # peguei a quantidade de valores que vão ser inseridos
x = 0 # criei uma variavel de contador
sAux= '' # crio uma variavel auxiliar
i = 0 # criei mais  uma variavel de contador 
nValores = []

# adicionando valores na lista
while x < nQuantidade:
    nValores[x].append(int(input()))
    x+=1

nCont = 0 # crio um contador
nLimite = len(nValores) # defino uma variável para ser usada como limete do meu contador
i = 0 # variável de contadore
nResultado = 0 # variável utilizada para guardar vaolor final

while nCont < nLimite:
    if nValores[nCont] == 0 and nValores[(nCont-1)] != 0: # testo se o valor é 0 ou 10
        del(nValores[(nCont-1)]) # deleto o valor anterior ao 0
        del(nValores[(nCont-1)]) # deleto o 0
        nCont-=2 # volto o contador 2 números antes para poder recomeçar
        nLimite-=2 # diminuo o limite
        
    nCont+=1

# del(nValores[0]) # deleto o primeiro valor, pois ele é ignorado na conta

# bloco de código para fazer a soma de todos os valores da lista
while i != len(nValores):
    nResultado = nResultado + int(nValores[i])
    i+=1

print(int(nResultado)) # exibição de resultado
