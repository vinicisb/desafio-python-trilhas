valorDaCompra = 1

while valorDaCompra != 0:
    valorDaCompra = float(input("Digite o valor da compra: "))
    if valorDaCompra == 0:
        break
    elif valorDaCompra < 0:
        print("Valor negativo, tente novamente")
        continue

    idade = int(input("Digite a idade do cliente: "))

    if idade >= 65:
        valorDaCompra = valorDaCompra * 0.8

    if valorDaCompra > 100:
        valorDaCompra = valorDaCompra * 0.9

    print(valorDaCompra)
