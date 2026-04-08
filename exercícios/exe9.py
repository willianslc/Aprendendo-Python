num_secreto = 7
palpite = 0

while palpite != num_secreto:
  palpite = int(input("Qual o seu palpite para adivinhar o número? "))

  if palpite < num_secreto:
    print("Você errou, é maior!")
  elif palpite > num_secreto:
    print("Você errou, é menor!")
  else:
    print("ACERTOU!")