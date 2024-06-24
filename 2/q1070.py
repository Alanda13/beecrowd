def main():
    num = int(input())
    calcular_impares_consec(num)

def calcular_impares_consec(num):
    contador = 0
    while contador < 6:
        if num % 2 != 0:
              print(num)
              contador += 1
        num += 1

main()

