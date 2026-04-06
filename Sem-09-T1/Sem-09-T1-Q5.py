print('''
    05. Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco).
    A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:

    • Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
    • Se 1 (um), escreva se o valor lido é par ou ímpar;
    • Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
    • Se 3 (três), escreva a divisão inteira do valor lido por 10;
    • Se 4 (quatro), escreva o quadrado do valor lido;
''')

def operacao_matematica(n):
    
    resto = n % 5

    if resto == 0:
        return 9 * n + 7, resto
    
    elif resto == 1:
        
        if n % 2 == 0:
            return 'par',  resto
        else:
            return 'ímpar', resto
        
    elif resto == 2:
        
        return 5 * (n ** 2) - 3 * n + 42, resto

    elif resto == 3:
        return n // 10, resto
    
    elif resto == 4:
        return n ** 2, resto
    
    else:
        raise ValueError('Digite uma das opcoes')

def main():
        
    i_n1 = int(input('Digite um numero inteiro: '))

    resultado,valor_do_resto = operacao_matematica(i_n1)

    print(f'O resto da divisão do numero digitado é {valor_do_resto} e o resultado da operação matematica de acordo com a tabela é: {resultado}')
    
if __name__ == '__main__':
    main()