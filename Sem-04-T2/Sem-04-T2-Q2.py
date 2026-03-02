'''Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa expressa apenas em dias. Considerar sempre os anos com 365 dias e os messes com 30 dias.

'''
print('Conversor de idade em dias totais')
anos = int(input('Anos: '))
mes = int(input('Meses: '))
dia = int(input('Dias: '))


print(f'Sua idade expressa em dias é: {(anos*365)+(mes*30)+dia} dias')