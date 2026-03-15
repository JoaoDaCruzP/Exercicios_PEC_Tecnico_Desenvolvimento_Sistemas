'''01. Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.'''

def conta_caracteres (palavra):
    valor =len(palavra)
    return valor

def main():
    
    entrada_palavra = input().strip()
    
    resultado = conta_caracteres(entrada_palavra)
    
    print(resultado)
    
if __name__ == '__main__':
    main()