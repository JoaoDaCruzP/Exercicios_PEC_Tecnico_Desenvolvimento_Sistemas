print('''
        05. Escreva um programa que leia três números e mostre na tela em ordem crescente.
      ''')

def crescente(n1,n2,n3):

    if n1 > n2 > n3:
        return n3,n2,n1
    if n1 > n3 > n2:
        return n2,n3,n1
    
    if n2 > n1 > n3:
        return n3,n1,n2
    if n2 > n3 > n1:
        return n1,n3,n2
    
    if n3 > n2 > n1:
        return n1,n2,n3
    if n3 > n1 > n2:
        return n2,n1,n3
        

def main():
    i_n1 = int(input('Digite o primeiro numero inteiro: '))

    i_n2 = int(input('Digite o segundo numero inteiro: '))

    i_n3 = int(input('Digite o terceiro numero inteiro: '))
    
    n1,n2,n3 = crescente(i_n1,i_n2,i_n3)
    
    print('Os numero em ordem Crescente é: ')
    print(n1)
    print(n2)
    print(n3)
if __name__ == '__main__':
    main()