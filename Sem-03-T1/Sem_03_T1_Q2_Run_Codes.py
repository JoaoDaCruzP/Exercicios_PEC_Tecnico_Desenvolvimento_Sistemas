'''Desenvolva um programa que pergunte a distância até um planeta em quilômetros e a velocidade da nave em km/h. Informe quantos dias e quantas horas a viagem levará, considerando 24 horas por dia.'''

dist = int(input().strip())

vel = int(input().strip()) 

tempo = (dist // vel)
resto = dist % vel
dias = tempo // 24
horas = tempo % 24
print(f'{dias} dias e {horas} horas')
