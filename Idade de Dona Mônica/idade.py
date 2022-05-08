nMonica = int(input())
nFilho1 = int(input())
nFilho2 = int(input())
nFilho3 = nMonica - (nFilho1 + nFilho2)

if nFilho1 > nFilho2:
    if nFilho1 > nFilho3:
        print(nFilho1)
    else:
        if nFilho3 > nFilho2:
            print(nFilho3)
        else:
            print(nFilho1)
else:
    if nFilho2 > nFilho3: 
        print(nFilho2)
    else:
        print(nFilho3)