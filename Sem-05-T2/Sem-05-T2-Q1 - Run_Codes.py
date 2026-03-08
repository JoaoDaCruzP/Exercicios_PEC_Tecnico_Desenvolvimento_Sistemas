'''01. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou o
valor booleano False (falso) caso contrário.'''

def valida (caractere):
    valor = caractere.lower() in 'aeiou'
    return valor

def main():
    entrada_caractere = input().strip()
    
    resultado = valida(entrada_caractere)
    print(resultado)
    
if __name__ == '__main__':
    main()