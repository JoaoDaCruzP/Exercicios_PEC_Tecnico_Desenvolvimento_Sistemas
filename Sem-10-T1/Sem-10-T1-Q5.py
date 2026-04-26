print(
    '''
  05. Escreva um programa que leia um conjunto de 5 números inteiros positivos e determine o maior deles.
    ''')

def main():
    maior = 0

    for i in range(5):
        num = int(input('Digite um numero: '))

        if num > maior:
            maior = num
    
    print(f'O maior numero digitado é : {maior}')

if __name__ == '__main__':
    main()