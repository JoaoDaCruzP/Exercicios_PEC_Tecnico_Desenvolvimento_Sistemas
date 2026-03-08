'''01. Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:

def calcular(a, b, c):
return 2 * a + 5 * b - c'''
def calcular (a,b,c):
    return 2 * a + 5 * b - c

def main():
    
    print('vamos calcular a função "2 * a + 5 * b - c"')
    print('Obs: Digite somente numeros inteiros!\n')
    
    entrada_v1 = int(input('Digite o valor de a: '))
    entrada_v2 = int(input('Digite o valor de b: '))
    entrada_v3 = int(input('Digite o valor de c: '))

    resultado = calcular(entrada_v1,entrada_v2,entrada_v3)
    print(f'O resultado da função é: {resultado}')
    
if __name__ == '__main__':
    main()