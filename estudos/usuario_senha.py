usuario = str(input("Informe o seu nome de usuário: ")).lower()
senha = str(input("Informe a sua senha:"))

if usuario == "admin" and senha == "1234":
    print("Acesso administrativo!")

elif usuario == "aluno" and senha == "unifecaf":
    print("Acesso autorizado!")
    
else:
    print("Acesso negado!")