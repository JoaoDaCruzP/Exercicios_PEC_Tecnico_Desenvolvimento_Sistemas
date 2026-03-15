'''
04. Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
• o maior número lido;
• o menor número lido;
• a média aritmética dos números lidos.
'''
def maior_lido(n1,n2,n3,n4,n5):
    maior = max(n1,n2,n3,n4,n5)
    return maior

def menor_lido(n1,n2,n3,n4,n5):
    menor = min(n1,n2,n3,n4,n5)
    return menor

def media(n1,n2,n3,n4,n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5
    return media

def main():
    print('Vamos verificar: * O maior numero; * menor numero; * A media de 5 numeros\n')
    entrada_n1 = int(input('Digite o valor 01: ').strip())
    entrada_n3 = int(input('Digite o valor 02: ').strip())
    entrada_n2 = int(input('Digite o valor 03: ').strip())
    entrada_n4 = int(input('Digite o valor 04: ').strip())
    entrada_n5 = int(input('Digite o valor 05: ').strip())
    
    result_maior = maior_lido(entrada_n1,entrada_n2,entrada_n3,entrada_n4,entrada_n5)
    result_menor = menor_lido(entrada_n1,entrada_n2,entrada_n3,entrada_n4,entrada_n5)
    result_media = media(entrada_n1,entrada_n2,entrada_n3,entrada_n4,entrada_n5)
    
    print(f'O maior numero é: {result_maior}\nO menor numero: {result_menor}\nA media dos valores é: {result_media}')
    
if __name__ == '__main__':
    main()