#Área esquerda

def main():
    O = input()

    matriz = []
    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)

    soma = 0
    cont = 0

    for i in range(12):
        for j in range(12):
            if j < 12 - i - 1: 
                soma += matriz[i][j]
                cont += 1

    if O == "S":
        print('{:.1f}'.format(soma))
    elif O == "M":
        media = soma / cont if cont > 0 else 0
        print('{:.1f}'.format(media))


main()