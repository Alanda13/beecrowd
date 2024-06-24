def main():
    X = int(input())
    Y = int(input())

    resultado = calcular_soma_impares(X,Y)
    print(resultado)
    

def calcular_soma_impares(X, Y):
    menor = min(X, Y)
    maior = max(X, Y)

    soma = 0
    
    if menor % 2 == 0:
        menor += 1
    
    while menor < maior:
        soma += menor
        menor += 2
    
    return soma


main()