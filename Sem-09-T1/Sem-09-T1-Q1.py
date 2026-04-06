print('''
    01. Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os
    valores lidos:

    • Todos os valores são diferentes;
    • Existem dois valores iguais e um diferente;
    • Todos os valores são iguais.
''')

def ler_numero(n1,n2,n3):

    if n1 == n2 == n3:
        return 'Todos os valores são iguais'
    
    elif n1 != n2 and n1 != n3 and n2 !=n3:
        return 'Todos os valores são diferentes'
    
    else:
        return 'Existem dois valores iguais e um diferente'

def main():

    i_num1 = int(input('Digite um numero inteiro: ').strip())
    i_num2 = int(input('Digite outro numero inteiro: ').strip())
    i_num3 = int(input('Digite mais um numero inteiro: ').strip())

    resultado = ler_numero(i_num1,i_num2,i_num3)

    print(resultado)

if __name__ == '__main__':
    main()