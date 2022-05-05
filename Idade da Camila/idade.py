nIdade1 = int(input()) # peguei o valor com um input, mas como número inteiro
nIdade2 = int(input()) # peguei o valor com um input, mas como número inteiro
nIdade3 = int(input()) # peguei o valor com um input, mas como número inteiro

#bloco para testar as restrições do código
def fnIdadeCamila():
    if nIdade1 >= 5 and nIdade2 >= 5 and nIdade3 >= 5 and nIdade1 <= 100 and nIdade2 <= 100 and nIdade3 <= 100:
            fnTestaIdade()
    else:
        return()

# bloco de código, com um teste miucioso para saber qual é a idade de camila
def fnTestaIdade():
    #esse bloco de código testa para saber qual é o do meio
    if nIdade3 > nIdade2 and nIdade3 < nIdade1:
        print(int(nIdade3)) # mostra a idade de camila
    elif nIdade2 > nIdade3 and nIdade2 < nIdade1:
        print(int(nIdade2)) # mostra a idade de camila
    elif nIdade1 > nIdade3 and nIdade1 < nIdade2:
        print(int(nIdade1)) # mostra a idade de camila
    elif nIdade3 < nIdade2 and nIdade3 > nIdade1:
        print(int(nIdade3)) # mostra a idade de camila
    elif nIdade2 < nIdade3 and nIdade2 > nIdade1:
        print(int(nIdade2)) # mostra a idade de camila
    elif nIdade1 < nIdade3 and nIdade1 > nIdade2:
        print(int(nIdade1)) # mostra a idade de camila

    # esse bloco de código testa se alguma das irmãs tem a idade igual
    elif nIdade1 == nIdade2:
        if nIdade3 > nIdade2:
            print(int(nIdade3)) # mostra a idade de camila
        else:
            print(int(nIdade2)) # mostra a idade de camila

    elif nIdade1 == nIdade3:
        if nIdade3 > nIdade2:
            print(int(nIdade3)) # mostra a idade de camila
        else:
            print(int(nIdade2)) # mostra a idade de camila
            
    elif nIdade3 == nIdade2:
        if nIdade3 > nIdade1:
            print(int(nIdade3)) # mostra a idade de camila
        else:
            print(int(nIdade1)) # mostra a idade de camila

    else:
        return()

fnIdadeCamila()