'''Escreva um programa que leia um preço e um valor percentual. Informe o preço com o aumento percentual e o preço com o desconto percentual. Por exemplo, se for lido um preço de 100.00 e o valor percentual de 5 o programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.'''

def acrescimo(valor,porcentagem):
    #vai calcular o acrescimo
    return valor+ ((valor / 100) * porcentagem)

def desconto(valor,porcentagem):
    #vai calcular o desconto
    return valor - ((valor / 100) * porcentagem)
    
def main():
    print('Vamos calcular o acrescimo e o desconto de um valor:\n')
    entrada_valor = float(input('Digite o valor desejado: '))
    entrada_porcentagem = float(input('Digite a porcentagem a ser aplicada: '))
    
    valor_com_acrescimo = acrescimo(entrada_valor, entrada_porcentagem)
    valor_com_desconto = desconto(entrada_valor, entrada_porcentagem)
    
    print(f'\nO valor total com acrescimo é R${valor_com_acrescimo:.2f}')
    print(f'\nO valor total com desconto é R${valor_com_desconto:.2f}')

if __name__ == '__main__':
    main()