numero = int(input("Digite um número de 2 a 9: "))
contador = 2

for contador in range(1, 11):
  resultado = numero * contador
  print(f"{numero} x {contador} = {resultado}")