nAlunos = int(input()) # peguei o valor com um input, mas um valor inteiro /  guarda a quantidade de alunos
sCamisetas = input() # peguei o valor com um input, mas um valor inteiro / guarda os tamanhos das camisetas
nPequena = int(input()) # peguei o valor com um input, mas um valor inteiro / guarda a quantidade solicitada de camisetas pequenas
nMedia = int(input()) # peguei o valor com um input, mas um valor inteiro / guara a quantidade solicatada de camisetas medias

def fnContaCamisa():
    if nAlunos >= 0 and nAlunos <= 1000: # teste de restrições
        if nPequena >= 0 and nPequena <= 1000 and nMedia >= 0 and nMedia <= 1000: # teste de restições 
            if nAlunos == (nPequena + nMedia): # teste de restições 
                nCamisas = list(sCamisetas.replace(" ", "")) # criando uma lista com os tamanhos das camisetas
                i = 0 # variável contador
                nNum1 = 0 # variável contador de camisetas pequenas
                nNum2 = 0 # variável contador de camisetas médias

                # bloco de códigos para quanto tem de cada camiseta
                while i < len(nCamisas): 
                    if nCamisas[i] == '1':
                        nNum1 += 1 # soma um nas pequqenas 
                    else:
                        nNum2 += 1 # soma um nas médias
                    i += 1
                if nPequena == nNum1 and nMedia == nNum2 and nAlunos == len(nCamisas): # teste de restrições
                    print('S') # resultado positvo
                else:
                    print('N') # resultado negativo
            else:
                print('N') # resultado negativo
        else:
                print('N') # resultado negativo
    else:
                print('N') # resultado negativo
    

fnContaCamisa()