idade = int(input("informe a sua idade: "))
renda = float(input("informe a sua renda: "))
score = int(input("informe o seu score: "))

if score > 1000:
    print("Informe um score válido")

elif idade >= 25 and renda >= 8000 and score >= 800:
    print("Parabéns um crédito premium foi aprovado para você")

elif idade >= 18 and renda >= 4000 and score >= 700:
    print("Parabéns um crédito avançado foi aprovado para você")

elif idade >= 18 and renda >= 2000 and score >= 500:
    print("Parabéns um crédito básico foi aprovado para você")

elif idade < 18:
    print("Infelizmente você não tem idade suficiente para solicitar um crédito")

elif renda < 2000:
    print("Infelizmente você não tem renda suficiente para solicitar um crédito")

elif score < 500:
    print("Infelizmente você não tem score suficiente para solicitar um crédito")

else:
    print("Infelizmente você não se enquadra em nenhum tipo de crédito disponível")