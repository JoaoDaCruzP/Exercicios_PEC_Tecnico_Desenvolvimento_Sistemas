'''
04. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.
'''
def verifica(caractere):
    return caractere.lower() in '0123456789' or 'a' <= caractere.lower() <= 'z'

def main():
    entrada_caractere = input()
    
    resultado = verifica(entrada_caractere)
    print(resultado)
    
if __name__ == '__main__':
    main()