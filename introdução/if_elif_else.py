aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digita o valor da nota 1: "))
nota2 = float(input("Digita o valor da nota 2: "))
nota3 = float(input("Digita o valor da nota 3: "))

nota_final = (nota1 + nota2 + nota3) / 3

if nota_final >= 7:
    print(f"{aluno} APROVADO(a) ficou com {nota_final:.1f} de média")
elif nota_final >= 5 and nota_final < 7:
    print(f"{aluno} precisará fazer a recuperação, pois ficou com {nota_final:.1f} de média")
else:
    print(f"{aluno} REPROVADO(a) ficou com {nota_final:.1f} de média ")

#O .2f ali nos prints onde a "nota_final" aparece é para controlar a quantidade de casas decimais irá aparecer após a vírgula

#Ali na linha 6 onde o calculo ocorre, devido a regra da matemática onde soma vem antes da divisão, devemos usar os parênteses
#para indicar ao Python que faça primeiro aquele calculo e depois faça a divisão.