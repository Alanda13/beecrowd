##Acima da diagonal principal
def main():
    matriz = []

    O = input() ##S para soma ou M para media

    for i in range(0, 12):
        matriz.append([])
        for j in range(0,12):
            matriz[i].append(0)

    for i in range(0,12):
        for j in range(0,12):
            matriz[i][j] = float(input())
    
    soma = 0
    for i in range(0, 12):
        for j in range(0, 12):
            if (i < j):     ##numero da coluna tem que ser maior que o numero da linha
                soma = soma + matriz[i][j]
    
    media = soma/66

    if (O == "S"):
        print("%.1f" %soma)
    elif(O == "M"):
        print("%.1f" %media)


main()