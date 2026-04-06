print('''
    04. Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a
    média. Considere duas casas decimais.
''')

def calcula_media(n1,n2,n3,n4,n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():

    i_n1 = int(input('Digite um numero: '))
    i_n2 = int(input('Digite um numero: '))
    i_n3 = int(input('Digite um numero: '))
    i_n4 = int(input('Digite um numero: '))
    i_n5 = int(input('Digite um numero: '))

    media = calcula_media(i_n1,i_n2,i_n3,i_n4,i_n5)

    print(f'Média: {media}')
    print('Notas maiores que a média: ')
    if i_n1 > media:
        print(i_n1, end=' ')
    if i_n2 > media:
        print(i_n2, end=' ')
    if i_n3 > media:
        print(i_n3, end=' ')
    if i_n4 > media:
        print(i_n4, end=' ')
    if i_n5 > media:
        print(i_n5, end=' ')

 
if __name__ == '__main__':
    main()