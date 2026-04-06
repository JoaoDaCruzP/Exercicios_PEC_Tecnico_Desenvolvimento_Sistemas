print('''
    02. Escreva um programa que leia dois valores e uma das seguintes operações a serem executadas (codificadas da
    seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa
    operação sobre os dois valores lidos.
''')

def operacao(n1,n2):
    adicao = n1 + n2

    subtracao = n1 - n2

    multiplicacao = n1 * n2

    divisao = n1 / n2
    
    return adicao,subtracao,multiplicacao,divisao

def main():

    i_num1 = int(input('Digite um numero inteiro: '))
    i_num2 = int(input('Digite outro numero inteiro: '))

    escolha = int(input('Escolha uma opção: '))
    

    soma,subtra,mult,div = operacao(i_num1,i_num2)

    if escolha == 1:
        print(f'Soma: {soma}')

    elif escolha == 2:
        print(f'Subtração: {subtra}')
    
    elif escolha == 3:
        print(f'Multiplicação: {mult}')
    
    elif escolha == 4:
        print(f'Divisão: {div}')

    else:
        raise ValueError('Digite uma opção valida')

if __name__ == '__main__':
    main()