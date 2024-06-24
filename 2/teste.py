def soma_impares(x, y):
    # Garante que x seja menor que y
    if x > y:
        x, y = y, x

    # Função para calcular a soma dos ímpares em uma sequência
    def soma_impares_sequencia(inicio, fim):
        n = (fim - inicio) // 2 + 1
        soma = n * (inicio + fim) // 2
        return soma

    # Calcula a soma dos ímpares entre x e y
    soma_total = soma_impares_sequencia(x + 1, y - 1)
    
    return soma_total

# Entrada dos valores de X e Y
x = int(input())
y = int(input())

# Chama a função para calcular a soma dos ímpares
resultado = soma_impares(x, y)

# Exibe o resultado
print(resultado)
