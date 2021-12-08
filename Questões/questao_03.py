""" 3) Modifique o programa abaixo para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, 
apenas os números ímpares.

fim = int(input("Digite o último número a imprimir:"))
x = 0
while x <= fim:
	print(x)
	x = x + 2
 """

x = 1
numeroEscolhido = int(input('Informe um número inteiro qualquer:'))
print('\n----------Os números ímpares até o numero escolhido %d são:\n' % (numeroEscolhido))
while x<=numeroEscolhido:
    if (x%2)==1:
        print(x)
    x +=1
