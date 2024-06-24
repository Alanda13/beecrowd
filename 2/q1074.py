def main():
    N = int(input())

    contador = 0


    while contador < N:
        numero = int(input())
        resultado = verificar_numero(numero)
        print(resultado)
        contador += 1

def verificar_numero(N):
    if N == 0:
        return 'NULL'
    elif N % 2 == 0:
        if N > 0:
            return "EVEN POSITIVE"
        else:
            return "EVEN NEGATIVE"
    else:
        if N > 0:
            return "ODD POSITIVE"
        else:
            return "ODD NEGATIVE"
        
main()