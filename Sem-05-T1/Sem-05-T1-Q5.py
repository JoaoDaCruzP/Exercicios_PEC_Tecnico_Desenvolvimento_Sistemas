'''05. Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. Por exemplo, se o número lido
for 5678 deverá ser mostrado 8765.'''
def converte_int(numero):
    numero = str(numero)
    numero_invertido = numero[::-1]
    return numero_invertido

def main():
    print('vamos inverter o numero que voce digitar!')
    
    entrada_numero = int(input('Digite um valor "inteiro" entre 1000 a 9999: '))
    
    resultado = converte_int(entrada_numero)
    
    print(f'O resultado da inversão do numero digitado é: {resultado}')

if __name__ == '__main__':
    main()