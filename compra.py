produto = str(input("Informe o nome do produto: "))
preco = float(input("Informe o valor do produto: "))
quantidade = int(input("Informe a quantidade desejada: "))
valor_total = preco * quantidade

print(f"--------------------------\nRESUMO DO PEDIDO\nProduto: {produto}\nValor unitário: R$ {preco:.2f}\nQuantidade: {quantidade}\nValor total: R$ {valor_total:.2f}\n--------------------------")

#att teste
