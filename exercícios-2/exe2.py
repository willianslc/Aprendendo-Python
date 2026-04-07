agenda = {}
nome = ""
telefone = ""

for i in range(3): #Range roda 3x o for
  nome = input("Digite nome do contato: ")
  telefone = input("Digite o telefone do contato: ")

  agenda[nome] = telefone

busca = input("Digite o nome de alguem cadastrado para retornar o telefone: ")
resultado_busca = agenda.get(busca, "Contato não cadastrado!")

print(f"{resultado_busca}")