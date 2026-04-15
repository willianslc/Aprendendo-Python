produtos = {
  "Arroz": 18.89,
  "Feijão": 7.45,
  "Ketchup": 9.99,
  "Tomate": 4.55,
  "Carne": 35.99,
  "sair": 0
}

total = 0

for i in range(5):
  produtos_select = input("Digite o nome do produto ou 'sair' para encerrar a compra: ")

  if produtos_select == "sair":
    print("Compra finalizada!")
    break
  
  total = total + produtos.get(produtos_select)

  print(f"Valor produto R${produtos[produtos_select]}")

    
print(f"Valor total da compra R${total:.2f}")