nIdade1 = int(input())
nIdade2 = int(input())
nIdade3 = int(input())

def fnIdadeCamila():
    if nIdade1 >= 5 and nIdade2 >= 5 and nIdade3 >= 5 and nIdade1 <= 100 and nIdade2 <= 100 and nIdade3 <= 100:
            fnTestaIdade()
    else:
        return()

def fnTestaIdade():
    #esse bloco de código testa para saber qual é o do meio
    if nIdade3 > nIdade2 and nIdade3 < nIdade1:
        print(int(nIdade3))
    elif nIdade2 > nIdade3 and nIdade2 < nIdade1:
        print(int(nIdade2))
    elif nIdade1 > nIdade3 and nIdade1 < nIdade2:
        print(int(nIdade1))
    elif nIdade3 < nIdade2 and nIdade3 > nIdade1:
        print(int(nIdade3))
    elif nIdade2 < nIdade3 and nIdade2 > nIdade1:
        print(int(nIdade2))
    elif nIdade1 < nIdade3 and nIdade1 > nIdade2:
        print(int(nIdade1))

    #esse bloco de código testa para mostrar a idade de camila se tiver algum valor igual 
    elif nIdade1 == nIdade2:
        if nIdade3 > nIdade2:
            print(int(nIdade3))
        else:
            print(int(nIdade2))

    elif nIdade1 == nIdade3:
        if nIdade3 > nIdade2:
            print(int(nIdade3))
        else:
            print(int(nIdade2))
            
    elif nIdade3 == nIdade2:
        if nIdade3 > nIdade1:
            print(int(nIdade3))
        else:
            print(int(nIdade1))

    else:
        return()

fnIdadeCamila()