'''Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas são 2, 3 e 5. Fórmula para o cálculo da média final é:

média ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10'''
print('Vamos calcular a media de 3 notas')
nota_1 = float(input('Digite a primeiro nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

print(f'A médias das notas digitadas é: {((nota_1* 2) + (nota_2 * 3) + (nota_3 * 5)) / 10}')