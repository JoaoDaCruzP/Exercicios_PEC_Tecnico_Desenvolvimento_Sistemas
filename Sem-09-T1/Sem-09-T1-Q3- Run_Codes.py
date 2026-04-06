'''
    03. Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. O programa deve
    inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a
    palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes
    a altura) do retângulo. Separe esses valores com um hífen.
'''
def calcula_retangulo(n1,n2):

    if n1 == n2:
        return 'QUADRADO'
    
    else:
        perimetro = (n1 * 2) + (n2 * 2)
        area = n1 * n2
        return f'{perimetro} - {area}'
        
def main():

    i_base = int(input())
    i_altura = int(input())

    resultado = calcula_retangulo(i_base,i_altura)
    
    print(resultado)

if __name__ == '__main__':
    main()