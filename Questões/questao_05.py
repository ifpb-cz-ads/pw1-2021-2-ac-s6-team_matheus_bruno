""" 5) Altere o programa abaixo para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2=4, ...

n = int(input("Tabuada de: "))
x = 1
while x <= 10:
	print(n + x)
	x = x + 1
 """
print('\nTabuada de multiplicação\n')
numero = int(input('Tabuada de: '))
x= 1
while x<=10:
    print(f'{x} X %d = %d' % (numero, (numero*x)))
    x+=1