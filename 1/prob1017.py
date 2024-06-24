def main():
    tempo = int(input())
    velocidade = int(input())

    distancia = velocidade * tempo

    qtd_litros = distancia / 12

    print(f"{qtd_litros:.3f}")

main()
