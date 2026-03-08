'''
02. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou o valor booleano False (falso) caso contrário.

'''

def verifica(caractere):
    return 'a' <= caractere.lower() <= 'z'

def main():
    entrada_caractere = input().strip()
    
    resultado = verifica(entrada_caractere)
    
    print(f'{resultado}')
    
if __name__ == '__main__':
    main()