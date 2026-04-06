'''
    05. Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco).
    A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:

    • Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
    • Se 1 (um), escreva se o valor lido é par ou ímpar;
    • Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
    • Se 3 (três), escreva a divisão inteira do valor lido por 10;
    • Se 4 (quatro), escreva o quadrado do valor lido;
'''

def operacao_matematica(n):
    
    resto = n % 5

    if resto == 0:
        return 9 * n + 7
    
    elif resto == 1:
        
        if n % 2 == 0:
            return 'par'
        else:
            return 'ímpar'
        
    elif resto == 2:
        
        return 5 * (n ** 2) - 3 * n + 42

    elif resto == 3:
        return n // 10
    
    elif resto == 4:
        return n ** 2
    
    else:
        raise ValueError('Digite uma das opcoes')

def main():
        
    i_n1 = int(input())

    resultado = operacao_matematica(i_n1)

    print(resultado)
    
if __name__ == '__main__':
    main()