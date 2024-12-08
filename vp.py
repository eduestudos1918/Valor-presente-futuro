def calcular_valor_futuro(pv, taxa_juros, periodos):

    fv = pv * (1 + taxa_juros) ** periodos
    return fv


def calcular_valor_presente(fv, taxa_juros, periodos):

    pv = fv / (1 + taxa_juros) ** periodos
    return pv


def main():
    print("Cálculos de Valor Presente e Valor Futuro")

    # Escolha qual cálculo fazer
    escolha = input("Para calcular o valor presente digite (1) e para calcular o valor futuro (2) ")

    if escolha == '1':
        # Calcular o Valor Presente
        fv = float(input("Digite o Valor Futuro (FV): "))
        taxa_juros = float(input("Digite a taxa de juros (em %): ")) / 100
        periodos = int(input("Digite o número de períodos: "))

        pv = calcular_valor_presente(fv, taxa_juros, periodos)
        print(f"O Valor Presente (PV) é: R${pv:.2f}")

    elif escolha == '2':
        # Calcular o Valor Futuro
        pv = float(input("Digite o Valor Presente (PV): "))
        taxa_juros = float(input("Digite a taxa de juros (em %): ")) / 100
        periodos = int(input("Digite o número de períodos: "))

        fv = calcular_valor_futuro(pv, taxa_juros, periodos)
        print(f"O Valor Futuro (FV) é: R${fv:.2f}")

    else:
        print("Opção inválida! Digite 1 para Valor Presente ou 2 para Valor Futuro.")


if __name__ == "__main__":
    main()
