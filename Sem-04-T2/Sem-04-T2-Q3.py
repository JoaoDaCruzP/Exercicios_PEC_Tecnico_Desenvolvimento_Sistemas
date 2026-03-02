'''Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit:

Fahrenheit = (Celsius x (9 / 5)) + 32'''
print('Conversor de Celcius para Fahrenheit')
g_celcius = float(input('Digite a temperatuda em Celcius (C°): '))

print(f'{g_celcius:.0f} Graus Celcius em Fahrenheit é: {(g_celcius * (9 /5))+ 32} Graus Fahrenheit')