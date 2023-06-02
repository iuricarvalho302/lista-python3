nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))

media = (nota1 + nota2) / 2

conceito = ""
mensagem = ""

if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    mensagem = "APROVADO"
else:
    mensagem = "REPROVADO"

print("Notas: ", nota1, nota2)
print("Média: ", media)
print("Conceito: ", conceito)
print("Situação: ", mensagem)