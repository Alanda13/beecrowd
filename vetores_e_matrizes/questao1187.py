##Área Superior
def main():
    O = input()

    matriz = []
    cont = 0

    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input())) ##prrenchendo a matriz
        matriz.append(linha)

    for i in range(0, 12):
        for j in range(0, 12):
            if (i < j and i < 12 - j - 1):
                soma = soma + matriz[i][j]
                cont = cont + 1
    media = soma / cont

    if(O == "S"):
        print('{:.1f}'.format(soma))
    elif(O == "M"):
        print('{:.1f}'.format(media))



main()