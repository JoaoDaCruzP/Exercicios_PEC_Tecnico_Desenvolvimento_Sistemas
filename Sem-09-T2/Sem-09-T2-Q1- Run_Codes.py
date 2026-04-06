'''
    01. Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira,
    3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.
'''

def ler_numero(n1):

    if n1 == 1:
        return 'domingo'
    
    elif n1 == 2:
        return 'segunda-feira'
    
    elif n1 == 3:
        return 'terça-feira'
    
    elif n1 == 4:
        return 'quarta-feira'
    
    elif n1 == 5:
        return 'quinta-feira'
    
    elif n1 == 6:
        return 'sexta-feira'
    
    elif n1 == 7:
        return 'sábado'
    
    else:
       return 'valor inválido'

def main():

    i_num1 = int(input().strip())
    
    resultado = ler_numero(i_num1)

    print(resultado)

if __name__ == '__main__':
    main()