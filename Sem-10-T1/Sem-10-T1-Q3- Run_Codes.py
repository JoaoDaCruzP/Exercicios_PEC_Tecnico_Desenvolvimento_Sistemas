'''
    03. Escreva um programa que leia um conjunto de 100 números inteiros e exiba o valor médio dos mesmos
    (com duas casas decimais).
'''

def main():

    media = 0
    contador = 0
    for i in range(100):

        num = int(input())
        media += num
        contador += 1

    media = media / contador

    print(media)

if __name__ == '__main__':
    main()