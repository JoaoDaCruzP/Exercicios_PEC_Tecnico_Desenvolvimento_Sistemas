'''Escreva um programa que leia um preço e um valor percentual. Informe o preço com o aumento percentual e o preço com o desconto percentual. Por exemplo, se for lido um preço de 100.00 e o valor percentual de 5 o programa deve mostrar que o preço com aumento é 105.00 e o preço com desconto é 95.00.'''

def acrescimo(v,p):
    #vai calcular o acrescimo
    return v + ((v / 100) * p)

def desconto(v,p):
    #vai calcular o desconto
    return v - ((v / 100) * p)
    
def main():
    
    valor = float(input())
    porcentagem = float(input())
    
    valor_com_acrescimo = acrescimo(valor, porcentagem)
    valor_com_desconto = desconto(valor, porcentagem)
    
    print(f'{valor_com_acrescimo:.2f}')
    print(f'{valor_com_desconto:.2f}')

if __name__ == '__main__':
    main()