print(
    '''
    02. Escreva um programa que leia o um conjunto de 100 números inteiros positivos e determine a quantidade
    de números pares e números ímpares contidos no mesmo.
    ''')

def main():
    
    par = 0
    impar = 0

    for i in range(100):

        num = int(input('Digite um numero: '))

        if num % 2 == 0:
            par += 1
        else:
            impar += 1
        
        
    print(f'Quantidade de numeros pares: {par}')
    print(f'Quantidade de numeros ímpares: {impar}')

if __name__ == '__main__':
    main()