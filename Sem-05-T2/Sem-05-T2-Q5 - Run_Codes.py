'''
05. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o que não é letra ou número) ou o valor booleano False (falso) caso contrário.
'''
def verifica(caractere):
    valida = caractere.lower() not in '1234567890abcdefghijklmnopqrstwuvxyz'
    return valida

def main():
    entrada_caractere = input()
    
    resultado = verifica(entrada_caractere)
    
    print(resultado)

if __name__ == '__main__':
    main()