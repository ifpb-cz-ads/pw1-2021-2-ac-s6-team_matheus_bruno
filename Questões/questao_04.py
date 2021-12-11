""" 4) Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3. """

x = 0
numeroEscolhido  = int(input('Informe um número inteiro qualquer:'))
print('\nOs números múltiplos de 3 até o número escolhido %d são:\n' %(numeroEscolhido))
while x<=numeroEscolhido:
    if (x%3)==0:
        print(x)
    x += 1