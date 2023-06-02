# Questão 3 - Cálculo de médias

# Criando o vetor para armazenar as médias
medias = []

# Obtendo as notas dos 10 alunos
for i in range(10):
    notas = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

# Calculando o número de alunos com média maior ou igual a 7.0
num_alunos_aprovados = sum(1 for media in medias if media >= 7.0)

# Exibindo o resultado
print("Número de alunos com média maior ou igual a 7.0:", num_alunos_aprovados)