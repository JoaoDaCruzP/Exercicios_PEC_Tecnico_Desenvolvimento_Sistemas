'''Você gostaria de saber quantos segundos se passaram desde a meia-noite? Escreva um programa que leia valores inteiros para hora, minuto e segundo. Em seguida, o programa deve calcular e imprimir quantos segundos se passaram no total desde a ultima meia-noite até a hora lida.'''

hora = int(input())
min = int(input())
seg = int(input())

tempo_total = ((hora * 60) *60) + (min * 60) + seg

print(f'{tempo_total}')