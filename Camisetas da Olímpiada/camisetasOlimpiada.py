import string


nAlunos = int(input())
sCamisetas = int(input())
nPequena = int(input())
nMedia = int(input())
sAux = str(sCamisetas)

def fnContaCamisa():
    nCamisas = list(sAux)
    i = 0
    nNum1 = 0
    nNum2 = 0
    while i < len(nCamisas):
        if nCamisas[i] == '1':
            nNum1 += 1
        else:
            nNum2 += 1
        i += 1
    if nPequena == nNum1 and nMedia == nNum2 and nAlunos == len(nCamisas):
        print("S")
    else:
        print("N")
    

fnContaCamisa()