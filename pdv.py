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

    if quantidade <= 0 or idade < 0:
        print("Tente novamente!")
        continue

    valorDaCompra = valorDaCompra * quantidade
    valorOriginal = valorDaCompra

    if idade >= 65:
        valorDaCompra = valorDaCompra * 0.8

    if valorDaCompra > 100:
        valorDaCompra = valorDaCompra * 0.9

    if "FIDELIDADE10" == cupom.upper():
        valorDaCompra = valorDaCompra * 0.9

    if quantidade > 3:
        valorDaCompra = valorDaCompra * 0.95

    valorDesconto = valorOriginal - valorDaCompra

    historico.append([valorOriginal, valorDesconto, valorDaCompra])

    print(f"Valor: R$ {valorDaCompra:.2f}")

print(f"Quantidade de compras: {len(historico)}")
print(f"Total bruto: R${sum(compra[0] for compra in historico):.2f}")
print(f"Total descontado: R${sum(compra[1] for compra in historico):.2f}")
print(f"Total final: R${sum(compra[2] for compra in historico):.2f}")

with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("--- RESUMO DO DIA ---\n")
    arquivo.write(f"Quantidade de compras: {len(historico)}\n")
    arquivo.write(f"Total bruto: R$ {sum(compra[0] for compra in historico):.2f}\n")
    arquivo.write(f"Total descontado: R$ {sum(compra[1] for compra in historico):.2f}\n")
    arquivo.write(f"Total final: R$ {sum(compra[2] for compra in historico):.2f}\n\n")
    
    arquivo.write("--- HISTÓRICO DE COMPRAS ---\n")
    for indice, compra in enumerate(historico):
        valor_orig = compra[0]
        desconto = compra[1]
        valor_final = compra[2]
        arquivo.write(f"Compra {indice + 1}: Original R$ {valor_orig:.2f} | Desconto R$ {desconto:.2f} | Final R$ {valor_final:.2f}\n")

print("Resumo salvo com sucesso no arquivo 'resumo.txt'!")