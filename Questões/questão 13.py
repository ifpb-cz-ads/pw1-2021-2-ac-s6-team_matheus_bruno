soma = 0
quantidade = 0
while True:
    n = int(input("Digite um numero inteiro: "))
    if n == 0:
        break
    soma = soma + n
    quantidade = quantidade + 1
print("A quantidade de numeros digitados foi:", quantidade)
print("A soma dos numeros foi: ", soma)
print(f"A média aritmetica foi: {soma/quantidade:10.2f}")