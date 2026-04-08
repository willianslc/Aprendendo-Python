def desconto(preco_roupa):
    if preco_roupa > 100:
       com_desconto = preco_roupa - 20
       return com_desconto
    else:
        return preco_roupa

com_desconto = desconto(150)
sem_desconto = desconto(80)

print("O valor da roupa com desconto ficou: R$", com_desconto)
print("O valor da roupa sem desconto ficou: R$", sem_desconto)