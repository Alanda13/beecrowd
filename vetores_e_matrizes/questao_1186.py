##Abaixo da diagonal secundária

def main():
    matriz = []
    cont = 0
    soma = 0
    O = input()
    resultado = 0
    
    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)

    for l in range(0, 12):
        for c in range(0, 12):
            if (l + c >= 12):
                cont = cont +1 

    media = soma/cont
            


    if (O == "S"):
         print('{:.1f}'.format(soma))
    elif(O == "M"):
        print('{:.1f}'.format(media))

main()