'''
    04. Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a
    média. Considere duas casas decimais.
'''
def calcula_media(n1,n2,n3,n4,n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():

    i_n1 = int(input())
    i_n2 = int(input())
    i_n3 = int(input())
    i_n4 = int(input())
    i_n5 = int(input())

    media = calcula_media(i_n1,i_n2,i_n3,i_n4,i_n5)

    print(media)
    if i_n1 > media:
        print(i_n1)
    if i_n2 > media:
        print(i_n2)
    if i_n3 > media:
        print(i_n3)
    if i_n4 > media:
        print(i_n4)
    if i_n5 > media:
        print(i_n5)

 
if __name__ == '__main__':
    main()