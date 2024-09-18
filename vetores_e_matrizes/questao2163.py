def encontrar_sabre_de_luz(matriz, linhas, colunas):
    tamanho_padrao = 3
    valor_central = 42
    valor_ao_redor = 7
    
    for i in range(1, linhas-1):
        for j in range(1, colunas-1):
            if matriz[i][j] == valor_central:
                if (matriz[i-1][j-1] == valor_ao_redor and matriz[i-1][j] == valor_ao_redor and matriz[i-1][j+1] == valor_ao_redor and
                    matriz[i][j-1] == valor_ao_redor and matriz[i][j+1] == valor_ao_redor and
                    matriz[i+1][j-1] == valor_ao_redor and matriz[i+1][j] == valor_ao_redor and matriz[i+1][j+1] == valor_ao_redor):
                    return (i + 1, j + 1)  
    return (0, 0)

def main():
    import sys
    entrada = sys.stdin.read
    dados = entrada().strip().split()
    
    indice = 0
    while indice < len(dados):
        numero_linhas = int(dados[indice])
        numero_colunas = int(dados[indice + 1])
        indice += 2
        
        if numero_linhas == 0 and numero_colunas == 0:
            break
        
        matriz = []
        for i in range(numero_linhas):
            matriz.append([int(dados[indice + j]) for j in range(numero_colunas)])
            indice += numero_colunas
        
        resultado = encontrar_sabre_de_luz(matriz, numero_linhas, numero_colunas)
        print(resultado[0], resultado[1])

if __name__ == "__main__":
    main()
