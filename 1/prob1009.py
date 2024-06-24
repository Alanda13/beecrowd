def main():
    nome = input()
    salario_fixo = float(input())
    total_vendas_mes = float(input())

    comissao = calcular_comissao(total_vendas_mes)

    total = salario_fixo + comissao
    print(f"TOTAL = R$ {total:.2f}")

def calcular_comissao(total_vendas_mes):
    comissao = (15/100) * total_vendas_mes
    return comissao

main()