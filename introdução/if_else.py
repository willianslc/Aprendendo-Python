nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Entrada liberada para {nome}!")
else:
    print(f"Você foi barrado! Você é menor de idade, você tem apenas {idade} anos")
