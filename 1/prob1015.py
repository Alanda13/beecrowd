import math

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

entrada_x1, entrada_y1 = input().split()
entrada_x2, entrada_y2 = input().split()

x1, y1 = float(entrada_x1), float(entrada_y1)
x2, y2 = float(entrada_x2), float(entrada_y2)

distancia = calcular_distancia(x1, y1, x2, y2)

print(f"{distancia:.4f}")

