'''01. Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.'''

def conta_caracteres (palavra):
    valor =len(palavra)
    return valor

def main():
    print('Vamos contar quantos caracteres existem na palavra digitada')
    entrada_palavra = input('digite o caractere desejado: ').strip()
    
    resultado = conta_caracteres(entrada_palavra)
    
    print(f'\nA palavra digitada possui {resultado} caracteres')
    
if __name__ == '__main__':
    main()