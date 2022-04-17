nAlunos = int(input())
sCamisetas = int(input())
nPequena = int(input())
nMedia = int(input())
sAux = str(sCamisetas)

def fnContaCamisa():
    if nAlunos >= 0 and nAlunos <= 1000:
        if nPequena >= 0 and nPequena <= 1000 and nMedia >= 0 and nMedia <= 1000:
            if nAlunos == (nPequena + nMedia):
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