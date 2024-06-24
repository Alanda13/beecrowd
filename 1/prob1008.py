def main():
    numero = int(input())
    horas_trab = int(input())
    valor_horas_trab = float(input())

    salario = horas_trab * valor_horas_trab

    print("NUMBER =", numero)
    print("SALARY = U$ {:.2f}".format(salario))

main()
