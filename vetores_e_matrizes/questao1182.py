##Coluna da matriz 

def main():
    matriz = []
    soma = 0

    coluna = int(input())
    operacao = input()

    for i in range (12):
        linha = []
        for j in range(12):
            numero = float(input())
            linha.append(numero)
        matriz.append(linha)
    
    for i in range(12):
        soma+=matriz[i][coluna]

    if operacao == 'S':
        print("%.1f" % soma)
    elif operacao == 'M':
        print("%.1f" % (soma / 12))




main()