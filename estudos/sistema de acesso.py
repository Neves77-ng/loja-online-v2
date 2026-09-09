idade = int(input("Informe a sua idade: "))
ingresso = input("Possui ingresso? (sim/não): ").lower()
lista_vip = input("Está na lista VIP? (sim/não): ").lower()
horario = int(input("Informe o horário atual (0 a 23): "))

if idade < 18:
    print("Acesso negado por ser menor de idade")

elif lista_vip == "sim" and horario <= 23:
    print("Acesso VIP aporoveite o evento!")

elif ingresso == "sim" and horario <= 22:
    print("Acesso comum aproveite o evento!")

elif (ingresso == "sim" or lista_vip == "sim") and horario <= 23:
    print("Acesso excepcional aproveite o evento!")

else:
    print("Acesso negado por nao atender aos critérios de idade, ingresso ou lista VIP, ou por estar fora do horário permitido.")