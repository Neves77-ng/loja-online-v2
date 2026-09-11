idade = int(input("Informe a idade do candidato:"))
estudante = str(input("O candidato é estudante? (Sim/Não)")).lower()
empregado = str(input("O candidato está empregado? (Sim/Não)")).lower()
cadastro = str(input("O candidato possui cadastro ativo? (Sim/Não)")).lower()

if idade < 25 and estudante == "sim" and cadastro == "sim":
    print("Benefício integral!")

elif idade < 25 and empregado == "sim" or cadastro == "sim":
    print("benefício parcial!")


elif idade >= 25 and cadastro == "sim":
    print("Benefício parcial!")

else:
    print("Sem benefício!")