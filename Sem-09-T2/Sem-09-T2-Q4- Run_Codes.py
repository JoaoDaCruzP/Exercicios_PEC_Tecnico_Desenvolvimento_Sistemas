'''
    04. Um sacolão está vendendo frutas com a seguinte tabela de preços:

        Até 5Kg                     Acima de 5Kg
    Morango R$ 2,50 por Kg          R$ 2,20 por Kg
    Maça R$ 1,80 por Kg             R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
    desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade
    (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

'''

def calcula_preco_sacolao(kg_morango, kg_maca):
   
    if kg_morango <= 5:
        preco_unit_morango = 2.50
    else:
        preco_unit_morango = 2.20
        
   
    if kg_maca <= 5:
        preco_unit_maca = 1.80
    else:
        preco_unit_maca = 1.50
        
    valor_bruto = (kg_morango * preco_unit_morango) + (kg_maca * preco_unit_maca)
    peso_total = kg_morango + kg_maca
    
   
    if peso_total > 8 or valor_bruto > 25.00:
        return valor_bruto * 0.90
    
    return valor_bruto

def main():
    i_morango = float(input())
    i_maca = float(input())
 
    resultado = calcula_preco_sacolao(i_morango, i_maca)
    
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()