##Abaixo da diagonal secundária

def main():
    matriz = []
    O = input()
    resultado = 0
    
    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input()))
        matriz.append(linha)

    vetor = []

    for l in range(1, 12):
        for c in range(12-l, 12):
            vetor.append(matriz[l][c])


    if (O == "S"):
        resultado = sum(vetor)
    elif(O == "M"):
        resultado = sum(vetor)/len(vetor)
    print('{:.1f}'.format(resultado))

main()