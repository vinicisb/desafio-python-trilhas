# Sistema de PDV - Desafio Nível 1

## O que o código faz
Este projeto é a implementação de um sistema básico de Ponto de Venda (PDV) que calcula descontos progressivos para clientes. O programa recebe o valor original dos produtos, a quantidade, a idade do cliente e um possível cupom de desconto, aplicando uma série de regras matemáticas para definir o valor final da compra. Ao fim do expediente (quando o usuário digita 0), o sistema gera um balanço diário mostrando o total vendido e o total de descontos concedidos.

## Como ele faz (Metodologia)
A lógica do script segue um fluxo sequencial dentro de um loop de repetição (`while`), funcionando da seguinte forma:
1. **Entrada e Validação:** Recebe o valor da compra, idade, quantidade e cupom. Se o valor for menor que zero, ou se a quantidade/idade forem inválidas, o sistema bloqueia a operação e pede os dados novamente.
2. **Cálculo Base:** Multiplica o valor unitário pela quantidade de itens.
3. **Desconto de Idade (Regra 1):** Se o cliente tiver 65 anos ou mais, aplica 20% de desconto sobre o valor total.
4. **Desconto de Valor (Regra 2):** Verifica o valor *após* o desconto de idade. Se for maior que R$ 100,00, aplica mais 10% de desconto.
5. **Bônus Implementados:** 
   - Aplica 10% de desconto extra se o cupom "FIDELIDADE10" for inserido.
   - Aplica 5% de desconto extra se a quantidade de itens comprados for maior que 3.
6. **Armazenamento:** Salva o valor original, o desconto total e o valor final de cada operação em uma lista (histórico).
7. **Encerramento:** Ao digitar `0` no valor da compra, o loop é quebrado e o sistema exibe o resumo financeiro do dia.
8. **Exportação (Com auxílio de IA):** A geração do arquivo `resumo.txt` (Bônus 3) foi desenvolvida em conjunto com Inteligência Artificial, utilizando a estrutura `with open()` para iterar sobre a lista de histórico e gravar o balanço final de forma segura em um arquivo de texto.

## Casos de Teste
Abaixo estão os casos validados para garantir a ordem correta das regras de desconto:

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |  

## Como rodar
Certifique-se de ter o Python instalado em sua máquina. Abra o terminal, navegue até a pasta `nivel_1` e execute o comando abaixo:

```bash
python pdv.py

