##Acima da diagonal secundária

def main():
    O = input()

    matriz = []

    for i in range(12):
        linha = []
        for j in range(12):
            linha.append(float(input())) ##prrenchendo a matriz
        matriz.append(linha)
    
    vetor = []

    for l in range(12):
        for c in range(12):
            if l + c < 11:
                vetor.append(matriz[l][c])

    resultado = 0
    
    if (O == "S"):
        resultado = sum(vetor)
    elif(O == "M"):
        resultado = sum(vetor)/len(vetor)
    print('{:.1f}'.format(resultado))

main()