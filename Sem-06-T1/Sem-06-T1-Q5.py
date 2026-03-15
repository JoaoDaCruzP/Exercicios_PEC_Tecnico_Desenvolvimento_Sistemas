'''
05. Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo preço de
etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. Escreva um programa que leia o valor de
uma compra e imprima três valores, todos com até duas casas decimais:
• Valor para pagamento à vista, com desconto de 9%.
• Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
• Valor da prestação para pagamento em 10 vezes, com 17% de juros.
'''
def a_vista(preco):
    valor = preco - (preco / 100) * 9
    return valor

def prestacao_5x(preco):
    valor = preco / 5
    return valor

def prestacao_10x(preco):
    parcela_s_juros = (preco / 10)
    parcela_total = parcela_s_juros + ((parcela_s_juros / 100) * 17)

    return parcela_total

def main():
    print('CALCULO DE JUROS DE UMA COMPRA! ')
    print('A vista tem desconto de 9%; Divida em 5 vezes sem juros e em 10 vezes tem juros de 17%\n')
    entrada_preco = int(input('Digite o valor da compra (R$): ').strip())
    
    resul_a_vista = a_vista(entrada_preco)
    resul_parcela_5x = prestacao_5x(entrada_preco)
    resul_parcela_10x = prestacao_10x(entrada_preco)
    
    print(f'Valor a vista: R${resul_a_vista:.2f}')
    print(f'5 parcelas de: R${resul_parcela_5x:.2f}')
    print(f'10 parcelas de: R${resul_parcela_10x:.2f}')

if __name__ == '__main__':
    main()