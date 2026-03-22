'''
    03. Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne
    a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.
'''

def ler_cor(cor):
    if cor[0] == 'V':
        return 'Siga'
    elif cor[0] == 'A':
        return 'Atenção'
    elif cor[0] == 'E':
        return 'Pare'
    else:
        return 'Entrada invalida'

def main():
    entrada_cor = input().strip().upper()
    
    resultado = ler_cor(entrada_cor)
    
    print(resultado)

if __name__ == '__main__':
    main()