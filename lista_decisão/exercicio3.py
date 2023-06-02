numero_macas = int(input("Digite o número de maçãs compradas: "))

if numero_macas < 12:
    custo_total = numero_macas * 1.30
else:
    custo_total = numero_macas * 1.00

print("O custo total da compra é:", custo_total)