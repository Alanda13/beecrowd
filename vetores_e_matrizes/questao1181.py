##linha na matriz

def main():
    matriz = []
    soma = 0

    indice = int(input())    ##pede que o usuário insira uma linha
    operacao = input()    ##operação S para soma ou M para média 

    for i in range (12):  ##cria as linhas da matriz
        linha = []   ##inicia uma lista vazia, armazena nela os numeros da linha atual
        for j in range(12):    ##preenche as colunas 
            numero = float(input())    ##pede um numero e esse numero será o valor da linha atual
            linha.append(numero)   ##vai adicionar o numero a lista linha
        matriz.append(linha)   ##adiciona a linha na matriz após preencher a linha com todos os numeros

    for a in range (12):
        for b in range(12):
            if a == indice:
                soma+=matriz[a][b]

    if operacao == 'S':
        print("%.1f" % soma)
    elif operacao == 'M':
        print("%.1f" % (soma / 12))

main()