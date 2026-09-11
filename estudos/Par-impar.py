numero = int(input("informe um número inteiro: "))

if numero % 2 == 0 and numero > 0:
    print("O número informado é par e é positivo!")

elif numero % 2 == 0 and numero < 0:
    print("O número informado é par e é negativo!") 

elif numero == 0:
    print("ZERO!")

elif numero % 2 == 1 and numero > 0:
    print("O número informado é impar e é positivo!")

else:
    print("O número informado é impar e é negativo!")


