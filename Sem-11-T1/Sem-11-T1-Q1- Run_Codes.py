'''
    Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre
    em quantos anos o valor acumulado será o dobro do valor inicial. Por exemplo:

        R$100,00 rendendo 8% ao ano irá
        dobrar em 10 anos.
        Início R$ 100.00
        1 ano R$ 108.00
        2 anos R$ 116.64
        3 anos R$ 125.97
        4 anos R$ 136.05
        5 anos R$ 146.93
        6 anos R$ 158.69
        7 anos R$ 171.38
        8 anos R$ 185.09
        9 anos R$ 199.90
        10 anos R$ 215.89

        R$100,00 rendendo 10% ao ano
        irá dobrar em 8 anos.
        Início R$ 100.00
        1 ano R$ 110.00
        2 anos R$ 121.00
        3 anos R$ 133.10
        4 anos R$ 146.41
        5 anos R$ 161.05
        6 anos R$ 177.16
        7 anos R$ 194.87
        8 anos R$ 214.36

        R$100,00 rendendo 15% ao ano
        irá dobrar em 5 anos.
        Início R$ 100.00
        1 ano R$ 115.00
        2 anos R$ 132.25
        3 anos R$ 152.09
        4 anos R$ 174.90
        5 anos R$ 201.14

        Dica: use repetição com teste no início
'''


def main():
    valor = float(input())
    por_rendimento = float(input()) / 100
    dobro = valor * 2
    anos = 0

    while valor < dobro:
        anos += 1
        valor += valor * por_rendimento

    print(anos)

    
if __name__ == '__main__':
    main()

