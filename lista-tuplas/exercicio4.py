# Idades e alturas dos alunos
idades = []
alturas = []

# Obtendo as idades e alturas dos alunos
for i in range(30):
    idade = int(input("Digite a idade do aluno {}: ".format(i+1)))
    altura = float(input("Digite a altura do aluno {}: ".format(i+1)))
    idades.append(idade)
    alturas.append(altura)

# Calculando a média de altura
media_altura = sum(alturas) / len(alturas)

# Contando alunos com mais de 13 anos e altura inferior à média
contador = 0
for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador += 1

# Exibindo o resultado
print("Número de alunos com mais de 13 anos e altura inferior à média:", contador)