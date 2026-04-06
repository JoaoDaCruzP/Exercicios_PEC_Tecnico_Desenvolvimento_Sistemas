print('''
    02. Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e
    100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.
''')

def particiona_numeros(numero):
    
    if (numero).isnumeric():
        numero = int(numero)
    else:
        raise ValueError('Digite apenas numeros')

    '''try:
        numero = int(numero)
    except:
        raise ValueError('Digite somente numeros!')'''


    n1 =  numero // 100000
    n2 = (numero % 100000) // 10000
    n3 = (numero % 10000) // 1000
    n4 = (numero % 1000) // 100   
    n5 = (numero % 100) // 10 
    n6 = (numero % 10) 

    if 0 <= numero <= 100000:
        return n1 + n2 + n3 + n4 + n5 + n6, 'Soma dos digitos do numero digitado: '

    else:
        return - 1, 'O resultado é: '

def main():

    i_numero = input()

    resultado,anuncio = particiona_numeros(i_numero)

    print(f'{anuncio} {resultado}')

if __name__ == '__main__':
    main()