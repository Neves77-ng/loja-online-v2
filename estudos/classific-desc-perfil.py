valor = float(input("Informe o valor da compra: "))
idade = int(input("Informe a sua idade: "))
estudante = str(input("O Sr. é estudante (sim/não): ")).lower()
desconto = int

if idade >= 60:
    desconto = 5

else:
    desconto = 0

if valor >= 500 or estudante == "sim":
    desconto = desconto + 10

elif valor >= 200:
    desconto = desconto + 5

elif valor < 200:
    desconto = 0

else:
    desconto = desconto

valor_desconto = valor*(desconto/100)
valor_final = valor - valor_desconto

print(f"Lhe foi concedido {desconto}% de desconto, valor final da sua compra é: R$ {valor_final:.2f}")