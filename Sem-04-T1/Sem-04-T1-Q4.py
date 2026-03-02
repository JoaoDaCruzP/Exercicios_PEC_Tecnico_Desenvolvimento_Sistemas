'''Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde a ultima meia-noite até a hora lida.'''
print('Você gostaria de saber quantos segundos se passaram desde a meia-noite?')
hora = int(input('Digite a quantidade de horas desejadas: '))
min = int(input('Digite a quantidade de minutos desejados: '))
seg = int(input('Digite a quantidade de segundos desejados: '))

tempo_total = ((hora * 60) *60) + (min * 60) + seg

print(f'Desde a meia noite, se passaram exatos: {tempo_total} segundos')