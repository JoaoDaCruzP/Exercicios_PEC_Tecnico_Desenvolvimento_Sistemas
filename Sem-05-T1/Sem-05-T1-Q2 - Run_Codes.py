'''Escreva um programa que ler o valor para um lado de um quadrado. Calcule o mostre a área e o perímetro desse quadrado.
'''

def calcular_area(l):
    #calcular a area do quadrado
    return l ** 2

def calcular_perimetro(l):
    #calcular o perimetro do quadrado
    return l * 4

def main():
    lado = float(input().strip())
    
    resultado_area = calcular_area(lado)
    resultado_perimetro = calcular_perimetro(lado)
    
    print(f'{resultado_area:10.4f}')
    print(f'{ resultado_perimetro:10.4f}')
    
if __name__ == '__main__':
    main()