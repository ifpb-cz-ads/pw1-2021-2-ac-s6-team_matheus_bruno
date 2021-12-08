""" 
7) Escreva um programa que leia dois números. Imprima o resultado da 
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e 
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação 
de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""

print('Multiplicação de dois números sem o operador de multiplicação\n')
numero1 = int(input('Informe o primeiro número inteiro:'))
numero2 = int(input('Informe o segundo número inteiro:'))
x = 1
resultado = 0

while x<=numero2: 
    resultado += numero1
    x+=1

print(f'{numero1} X {numero2} = {resultado}')