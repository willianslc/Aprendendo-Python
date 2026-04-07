salario = float(input("Digite o valor do seu salario:"))

if salario <= 3000.00:
    print("Seu salario corresponde a de uma pessoa de nível Júnior")
elif salario <= 6000.00:
    print("Seu salario corresponde a de uma pessoa de nível Pleno")
elif salario <= 12000.00:
    print("Seu salario corresponde a de uma pessoa de nível Senior")
else:
    print("Hummmm... Acima de 12k vc já é um GERENTE! Parabéns!")


#IF => Se algo for assim faça...
#ELIF => Se não, se for dessa outra forma aqui faça isso...
#ELSE => Se não for de nenhuma das forma acima ai faça isso...