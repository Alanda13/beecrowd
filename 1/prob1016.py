def main():
    distancia = int(input())


    velocidade_x = 60  
    velocidade_y = 90  

    velocidade_relativa = velocidade_y - velocidade_x

    tempo_em_horas = distancia / velocidade_relativa

    tempo_em_minutos = int(tempo_em_horas * 60)

    print(f"{tempo_em_minutos} minutos")

main()
