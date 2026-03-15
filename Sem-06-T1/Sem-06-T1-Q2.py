'''02. Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.'''


def caracter_para_codigo_numerico (caractere):
    valor = ord(caractere)
    return valor

def main():
    print('CONVERSOR DE CARACATERE PARA CODIGO NUMERICO')
    entrada_caractere = input('Digite um caractere: ')
    
    resultado = caracter_para_codigo_numerico(entrada_caractere)
    
    print(f'O codigo numerico do caractere digitado é: {resultado}')
    
if __name__ == '__main__':
    main()
