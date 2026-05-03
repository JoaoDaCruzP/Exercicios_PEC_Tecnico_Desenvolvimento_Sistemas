print('''
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
''')

def main():
    hamburguer = 5.50
    cheeseburguer = 6.80
    misto_quente = 4.50
    americano = 7.00
    queijo_prado = 4.00

    soma = 0

    while True:
        print('CARDÁPIO')
        print('[H] Hamburger R$ 5.50')
        print('[C] Cheeseburger  6.80')
        print('[M] Misto Quente R$ 4.50')
        print('[A] Americano R$ 7.00')
        print('[Q] Queijo Prato R$ 4.00')
        print('[X] PARA TOTAL DA CONTA')

        opcao = input('Digite a letra de seu pedido: ').strip().upper()

        if opcao[0] == 'H':
            soma += hamburguer
            print('hamburguer adicionado ao carrinho!')
        if opcao[0] == 'C':
            soma += cheeseburguer
            print('cheeseburguer adicionado ao carrinho!')
        if opcao[0] == 'M':
            soma += misto_quente
            print('misto_quente adicionado ao carrinho!')
        if opcao[0] == 'A':
            soma += americano
            print('americano adicionado ao carrinho!')
        if opcao[0] == 'Q':
            soma += queijo_prado
            print('queijo_prado adicionado ao carrinho!')
        if opcao[0] == 'X':
            encerrar = input('Tem certeza que deseja encerrar o pedido? [s] ou [n]: ').upper().split()
            if encerrar[0] == 'S':
                break
            else:
                continue

    print(f'O valor total do seu pedido é: R$ {soma:.2f}'.replace('.',','))

if __name__ == '__main__':
    main()