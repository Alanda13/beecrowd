def main():

    codigo_peca_1, num_peca_1, valor_unitario_peca_1 = map(float, input().split())
    codigo_peca_2, num_peca_2, valor_unitario_peca_2 = map(float, input().split())

    valor = (num_peca_1 * valor_unitario_peca_1) + (num_peca_2 * valor_unitario_peca_2)

    print(f"VALOR A PAGAR: R$ {valor:.2f}")
main()
