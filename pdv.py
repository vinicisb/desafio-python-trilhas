valorDaCompra = 1
historico = []

while valorDaCompra != 0:
    valorDaCompra = float(input("Digite o valor da compra: "))
    if valorDaCompra == 0:
        break
    elif valorDaCompra < 0:
        print("Valor negativo, tente novamente")
        continue

    idade = int(input("Digite a idade do cliente: "))
    quantidade = int(input("Digite a quantidade: "))
    cupom = input("Digite o seu cupom: ")

    valorDaCompra = valorDaCompra * quantidade
    valorOriginal = valorDaCompra

    if "FIDELIDADE10" == cupom.upper():
        valorDaCompra = valorDaCompra * 0.9

    if idade >= 65:
        valorDaCompra = valorDaCompra * 0.8

    if valorDaCompra > 100:
        valorDaCompra = valorDaCompra * 0.9


    if quantidade > 3:
        valorDaCompra = valorDaCompra * 0.95

    valorDesconto = valorOriginal - valorDaCompra

    if quantidade == 0:
        continue
    elif quantidade < 0:
        print("Quantidade invalida, tente novamente!")
        continue
    else:
        historico.append([valorOriginal, valorDesconto, valorDaCompra])

    print(f"Valor: {valorDaCompra}")

print(f"Quantidade de compras: {len(historico)}")
print(f"Total bruto: {sum(compra[0] for compra in historico):.2f}")
print(f"Total descontado: {sum(compra[1] for compra in historico):.2f}")
print(f"Total final: {sum(compra[2] for compra in historico):.2f}")