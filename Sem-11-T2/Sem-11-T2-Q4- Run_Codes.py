'''
    04. O cardápio de uma casa de lanches, especializada em sanduíches, é dado abaixo.

        CÓDIGO PRODUTO PREÇO (R$)
        =========================
        H Hamburger 5.50
        C Cheeseburger 6.80
        M Misto Quente 4.50
        A Americano 7.00
        Q Queijo Prato 4.00
        X PARA TOTAL DA CONTA

        Escreva um programa que leia o código de vários itens comprados por um freguês e acumule o total da
        compra. Ao finalizar com “X”, exiba o total a pagar.

        Observações:
            • Se for informada uma opção que não está no menu deve mostrar a mensagem “Opção
            inválida.”.
            • Enquanto o código não for 'X' o programa deve continuar lendo os itens.
            Dica: Use upper() para ignorar a diferenças entre maiúscula e minúsculas; Use [0] para garantir que
            apenas o primeiro caractere digitado seja considerado. Por exemplo:
            codigo = input('Código: ').upper()[0]
'''

def main():
    hamburguer = 5.50
    cheeseburguer = 6.80
    misto_quente = 4.50
    americano = 7.00
    queijo_prado = 4.00

    soma = 0

    while True:
        print('CÓDIGO  PRODUTO         PREÇO (R$)')
        print('H       Hamburger       5,50')
        print('C       Cheeseburger    6,80')
        print('M       Misto Quente    4,50')
        print('A       Americano       7,00')
        print('Q       Queijo Prato    4,00')
        print('X       PARA TOTAL DA CONTA')

        opcao = input().strip().upper()

        if opcao[0] == 'H':
            soma += hamburguer
        elif opcao[0] == 'C':
            soma += cheeseburguer
        elif opcao[0] == 'M':
            soma += misto_quente
        elif opcao[0] == 'A':
            soma += americano
        elif opcao[0] == 'Q':
            soma += queijo_prado
        elif opcao[0] == 'X':
            break
        else:
            print('Opção inválida.')
    print(f'{soma:.2f}')

if __name__ == '__main__':
    main()