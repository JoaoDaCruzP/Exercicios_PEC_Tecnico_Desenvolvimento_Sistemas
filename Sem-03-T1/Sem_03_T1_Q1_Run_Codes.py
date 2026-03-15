'''01. Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre
quantas fatias cada um recebe e quantas sobram.'''

entrada_n1 = int(input().strip())

entrada_n2 = int(input().strip())

#REALIZA A OPERAÇÃO
div_sem_resto = entrada_n1 // entrada_n2
resto = entrada_n1 % entrada_n2

print(div_sem_resto)
print(resto)
