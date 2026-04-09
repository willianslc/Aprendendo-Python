"""""
Sistema de Votação: Crie um programa que simule uma votação com 3 candidatos. 
Use um dicionário para contar os votos e, ao final, mostre quem ganhou.
"""""

candidatos = {
  "Maria": 0,
  "João": 0,
  "Paulo": 0
}

for i in range(5):
  votacao = input("Digite o nome do seu candidato: ")
  candidatos[votacao] = candidatos[votacao] + 1
  
vencedor = max(candidatos, key = candidatos.get)
print(f"O vencedor foi {vencedor} com {candidatos[vencedor]} votos!")
