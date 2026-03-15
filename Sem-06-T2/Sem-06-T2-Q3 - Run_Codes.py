'''
03. Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total!
Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.
'''

def calcular_preco_total(v1,v2):
    resultado = (v1 * 3) + (v2 * 2)
    return resultado

def main():
    #preciso saber qual o preço das frutas
    entrada_preco_maca = float(input().strip())
    entrada_preco_banana = float(input().strip())
    
    total = calcular_preco_total(entrada_preco_maca,entrada_preco_banana)
    
    print(f'{total:.2f}')
    
if __name__ == '__main__':
    main()