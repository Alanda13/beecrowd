##Abbaixo da diagonal principal

def main():
    matriz = []
    soma = 0
    O = input() ##S para soma ou M para media

    for i in range(0, 12):
        matriz.append([])
        for j in range(0,12):
            matriz[i].append(0)

    for i in range(0,12):
        for j in range(0,12):
            matriz[i][j] = float(input())

    for i in range(0,12):
        for j in range(0,12):
            if (j < i): ##numero da linha tem que ser maior que o numero da coluna
                soma = soma + matriz[i][j]
    
    media = soma / 66

    if (O == "S"):
        print("%.1f" %soma)
    elif(O == "M"):
        print("%.1f" %media)

main()