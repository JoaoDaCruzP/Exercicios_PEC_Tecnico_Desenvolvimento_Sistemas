'''Escreva um programa que leia dois valores e mostre na tela, nessa ordem:

a. A soma dos números;

b. A concatenação das strings;

c. A multiplicação dos números;

d. A multiplicação como strings;

e. A divisão dos números;

f. A divisão inteira dos números;

g. A exponenciação;

h. O módulo (resto).'''
print('Vamos fazer algumas operações numericas? ')
valor_1 = float(input('Digite um valor numerico: '))
valor_2 = float(input('Digite outro valor numerico: '))
print(f'A soma dos números: {valor_1 + valor_2}')
print(f'A concatenação das strings: {str(valor_1) + str(int(valor_2))}')
print(f'A multiplicação dos números: {valor_1 * valor_2}')
print(f'A multiplicação como strings: {str(valor_1) * int(valor_2)}')
print(f'A divisão dos números: {valor_1 / valor_2}')
print(f'A divisão inteira dos números: {valor_1 // valor_2}')
print(f'A exponenciação: {valor_1 ** valor_2}')
print(f'O módulo (resto): {valor_1 % valor_2}')