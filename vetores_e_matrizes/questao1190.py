#Area Direita


def main():
    O = input().strip

    matriz = []

    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)
    
    soma = 0
    contador = 0

    for i in range(12):
        for j in range(12):
            if j > i:
                soma += matriz[i][j]
                contador += 1

    if O == "S":
        print('{:.1f}'.format(soma))
    elif O == "M":
        media = soma / contador if contador > 0 else 0
        print('{:.1f}'.format(media))
    else:
        print()

main()