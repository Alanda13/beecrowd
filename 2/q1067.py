def main():
    x = int(input())
    imprimir_impares(x)

def imprimir_impares(x):
    numero = 1
    while numero <= x:
        if numero % 2 != 0:
            print(numero)
        numero += 2  

main()
