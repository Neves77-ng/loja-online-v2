nota = float(input("Informe a nota do estudante: (0 a 10)"))
freq = float(input("Informe a frequência do estudante: (0 a 100) "))

if nota > 10 or freq > 100:
    print("Informações invalidas!")

elif nota >= 9 and freq >= 90:
    print("Aprovado com excelencia!")

elif nota >= 7 and freq >= 75:
    print("Aprovado, Muito bem!")

elif nota >= 5 and freq >= 75:
    print("Aprovado! Você fez um bom trabalho mas pode melhorar!")

else:
    print("Reprovado!")