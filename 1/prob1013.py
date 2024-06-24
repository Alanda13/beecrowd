def main():
    valores = input().split()
    a, b, c = map(int, valores)

    maior = encontrar_maior_tresnum(a,b, c)

    print(f"{maior} eh o maior")


def encontrar_maior(a, b):
    return (a + b + abs(a - b)) // 2

def encontrar_maior_tresnum(a, b, c):
    maior_ab = encontrar_maior(a, b)
    maior = encontrar_maior(maior_ab, c)
    return maior

main()