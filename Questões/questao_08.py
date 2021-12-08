""" 
8) Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, 
assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que 
podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

"""

print('\nDivisão de dois números inteiro sem utilizar o operador de divisão de de resto\n')

numero1 = int(input('Informe o primeiro número inteiro:'))
numero2 = int(input('Informe o segundo número inteiro:'))
x = 0
resto = 0
dividendo = numero1
while numero1>=numero2:
    numero1-=numero2
    resto = numero1
    x+=1
print(f'{dividendo} ÷ {numero2} = Quociente: {x} Resto: {resto}')