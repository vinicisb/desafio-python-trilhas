valorDaCompra = 1
historico = []

while valorDaCompra != 0:
    valorDaCompra = float(input("Digite o valor da compra: "))
    if valorDaCompra == 0:
        break
    elif valorDaCompra < 0:
        print("Valor negativo, tente novamente")
        continue

    valorOriginal = valorDaCompra
    idade = int(input("Digite a idade do cliente: "))

    if idade >= 65:
        valorDaCompra = valorDaCompra * 0.8

    if valorDaCompra > 100:
        valorDaCompra = valorDaCompra * 0.9
    valorDesconto = valorOriginal - valorDaCompra
    historico.append([valorOriginal, valorDesconto, valorDaCompra])

    print(valorDaCompra)

print(f"Quantidade de compras: {len(historico)}")
print(f"Total bruto: {sum(compra[0] for compra in historico):.2f}")
print(f"Total descontado: {sum(compra[1] for compra in historico):.2f}")
print(f"Total final: {sum(compra[2] for compra in historico):.2f}")