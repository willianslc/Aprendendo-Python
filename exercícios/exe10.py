"""""
Lista de Compras Dinâmica: Crie um programa que permita ao usuário
inserir itens em uma lista até que ele digite "sair". 
No final, exiba a lista em ordem alfabética.
"""""

lista_produtos = []
produtos = ""

while produtos != "sair":
  produtos = input("Insira o nome do produto (Ou digite sair para encerrar): ")

  if produtos != "sair":
    lista_produtos.append(produtos)
  else:
    print("Sistema encerrado!")

lista_produtos.sort()
print(f"Sua lista de produtos ficou assim: {[lista_produtos]}")