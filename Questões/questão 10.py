deposito = float(input("Q o deposito inicial: "))
taxa = float(input("Insira a taxa de juros: "))
mes = 1
saldo = deposito
while mes <= 12:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"O saldo do mês {mes} é de R${saldo:5.2f}.")
    mes = mes + 1
print(f"O ganho obtido com os juros foi de R${saldo-deposito:8.2f}.")