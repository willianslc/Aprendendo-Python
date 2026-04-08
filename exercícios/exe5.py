escola = [
  {"nome": "Laura", "nota": 8},
  {"nome": "Romulo", "nota": 5},
  {"nome": "Natalia", "nota": 10}
]

for aluno in escola:
    if aluno["nota"] > 7:
        print(f"{aluno["nome"]}: APROVADO!")
    else:
        print(f"{aluno["nome"]}: REPROVADO!")





