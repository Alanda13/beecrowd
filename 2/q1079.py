def main():
    n = int(input())
    contador = 0
    while contador < n:
        n1, n2, n3 = map(float, input().split())
        media = calcular_media(n1, n2, n3)
        print(f'media ponderada: {media:.2f}')

def calcular_media(n1, n2, n3):
    media_ponderada = (n1 * 2 + n2 * 3 + n3 * 5) / (2 + 3 + 5)
    return media_ponderada


main()