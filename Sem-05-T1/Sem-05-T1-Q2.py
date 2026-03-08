'''Escreva um programa que ler o valor para um lado de um quadrado. Calcule o mostre a área e o perímetro desse quadrado.
'''

def calcular_area(lado):
    #calcular a area do quadrado
    return lado ** 2

def calcular_perimetro(lado):
    #calcular o perimetro do quadrado
    return lado * 4

def main():
    print('Vamos calcular a area e o perimetro de um quadrado')
    
    entrada_lado = float(input('Digite o numero desejado: ').strip())
    
    resultado_area = calcular_area(entrada_lado)
    resultado_perimetro = calcular_perimetro(entrada_lado)
    
    print(f'O resultado da area do quadrado é {resultado_area:10.4f}m²')
    print(f'O resultado do perimetro do quadrado é {resultado_perimetro:10.4f}m')
    
if __name__ == '__main__':
    main()