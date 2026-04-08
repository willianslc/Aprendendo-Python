personagem = {
  "nome": "Jack",
  "HP": 100
}

def receber_dano(vida_atual, valor_dano):
    return vida_atual - valor_dano

personagem["HP"] = receber_dano(personagem["HP"], 50)
print(personagem)