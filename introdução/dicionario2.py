item = {
  "nome": "Potion HP",
  "quantidade": 5,
  "valor_cura": 300
}

item["quantidade"] = item["quantidade"] - 1
item["valor_cura"] = 50

print("Você agora tem", item["quantidade"], "unidades de Potion HP e", item["valor_cura"], "a mais na cura da Potion HP")



filme = {
  "titulo": "Star Wars",
  "ano": 1977,
  "diretor": "George Lucas"
}

print(filme.values())
print(filme.keys())
print(filme.items())

