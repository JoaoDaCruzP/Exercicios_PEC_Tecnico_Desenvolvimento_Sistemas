'''02. Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.'''


def caracter_para_codigo_numerico (caractere):
    valor = ord(caractere)
    return valor

def main():
    
    entrada_caractere = input()
    
    resultado = caracter_para_codigo_numerico(entrada_caractere)
    
    print(resultado)
    
if __name__ == '__main__':
    main()

