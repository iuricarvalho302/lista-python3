numero_conta = input("Digite o número da conta do cliente: ")
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    mensagem = "Saldo Positivo"
else:
    mensagem = "Saldo Negativo"

print("Saldo Atual: ", saldo_atual)
print("Mensagem: ", mensagem)