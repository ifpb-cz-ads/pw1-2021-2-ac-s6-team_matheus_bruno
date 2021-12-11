""" 
6) Modifique o programa anterior de forma que o 
usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
"""
print('\nTabuada de multiplicação\n')
tabuada = int(input('Tabuada de: '))
comeco = int(input('Informe o inicio da tabuada:'))
fim = int(input('Informe o fim da tabuada:'))

while comeco<=fim:
    print(f'{comeco} X {tabuada} = %d' %((comeco * tabuada)))
    comeco+=1

