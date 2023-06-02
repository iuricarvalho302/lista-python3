# Lendo um vetor de 5 números inteiros
vetor = []
for i in range(5):
    numero = int(input("Digite o número {}: ".format(i+1)))
    vetor.append(numero)

# Exibindo os números
print("Números digitados:", vetor)
1