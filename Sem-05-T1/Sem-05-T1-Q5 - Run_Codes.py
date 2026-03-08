'''05. Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. Por exemplo, se o número lido
for 5678 deverá ser mostrado 8765.'''
def converte_int(n):
    n = str(n)
    n_invertido = n[::-1]
    return n_invertido

def main():
    numero = int(input())
    
    resultado = converte_int(numero)
    
    print(resultado)

if __name__ == '__main__':
    main()