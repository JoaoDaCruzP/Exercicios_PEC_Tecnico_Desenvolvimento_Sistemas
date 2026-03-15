'''
01. Um mago precisa misturar duas substâncias para criar uma poção. Peça ao usuário os dois volumes (em ml) e exiba o total da poção.
'''


entrada_n1 = float(input().strip())
entrada_n2  = float(input().strip())

#REALIZA A OPERAÇÃO
soma = entrada_n1 + entrada_n2

#MOSTRA O RESULTADO
print(f'{soma:.2f}')