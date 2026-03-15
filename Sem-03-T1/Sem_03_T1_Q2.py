'''Desenvolva um programa que pergunte a distância até um planeta em quilômetros e a velocidade da nave em km/h. Informe quantos dias e quantas horas a viagem levará, considerando 24 horas por dia.'''

#captura a entrada da distancia digitada pelo usuario
dist = int(input('Digite a distancia do planeta escolhido: ').strip())
#captura a entrada da velocidade digitada pelo usuario
vel = int(input('Digite a velocidade que a nave vai viajar: ').strip()) 

tempo = (dist // vel) #divisao sem resto entre distancia e velocidade
resto = dist % vel # resto da divisao entre distancia e velocidade
dias = tempo // 24 #divide o tempo sem resto por 24 horas para obter a quantidade de dias necessarios
horas = tempo % 24 #recebe  o resto da divisao por 24 para obter as horas necessarios
print(f'{dias} dias e {horas} horas') #printa resultado
