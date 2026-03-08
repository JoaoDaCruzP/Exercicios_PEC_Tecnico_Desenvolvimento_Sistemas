'''01. Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:

def calcular(a, b, c):
return 2 * a + 5 * b - c'''
def calcular (a,b,c):
    return 2 * a + 5 * b - c

def main():
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())

    resultado = calcular(v1,v2,v3)
    print(resultado)
    
if __name__ == '__main__':
    main()