'''Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. Considerar sempre os anos com 365 dias e os messes com 30 dias.

'''

anos = int(input())
mes = int(input())
dia = int(input())


print(f'{(anos*365)+(mes*30)+dia}')