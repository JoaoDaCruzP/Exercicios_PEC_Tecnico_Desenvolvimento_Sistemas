'''Escreva um programa que leia dois valores e mostre na tela, nessa ordem:

a. A soma dos números;

b. A concatenação das strings;

c. A multiplicação dos números;

d. A multiplicação como strings;

e. A divisão dos números;

f. A divisão inteira dos números;

g. A exponenciação;

h. O módulo (resto).'''

valor_1 = float(input())
valor_2 = float(input())
print(f'{valor_1 + valor_2}')
print(f'{str(valor_1) + str(int(valor_2))}')
print(f'{valor_1 * valor_2}')
print(f'{str(valor_1) * int(valor_2)}')
print(f'{valor_1 / valor_2}')
print(f'{valor_1 // valor_2}')
print(f'{valor_1 ** valor_2}')
print(f'{valor_1 % valor_2}')