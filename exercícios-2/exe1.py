"""""
DESAFIO
Analisador de Temperaturas:** Peça 7 temperaturas (uma para cada dia da semana) 
e guarde-as em uma lista. O programa deve calcular a média, 
a maior e a menor temperatura.
"""""

temperaturas = []


temperaturas.append(float(input("Informe a temperatura da segunda-feira: ")))
temperaturas.append(float(input("Informe a temperatura da terça-feira: ")))
temperaturas.append(float(input("Informe a temperatura da quarta-feira: ")))
temperaturas.append(float(input("Informe a temperatura da quinta-feira: ")))
temperaturas.append(float(input("Informe a temperatura da sexta-feira: ")))
temperaturas.append(float(input("Informe a temperatura da sabado: ")))
temperaturas.append(float(input("Informe a temperatura da domingo: ")))

media = sum(temperaturas) / 7 # A função sum, soma todos os números da lista automaticamente

print(f"A média das temperaturas para essa semnana foi {media:.1f} e as temperaturas máximas e mínimas fora max de {max(temperaturas)} e min de {min(temperaturas)}")
