'''
03. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma CONSOANTE ou o valor booleano False (falso) caso contrário.

'''

def verifica(caractere):
    return caractere.lower() in 'bcdfghjklmnpqrstvwxyz'

def main():
    
    entrada_caractere = input()
    
    resultado = verifica(entrada_caractere)
    
    print(resultado)
    
if __name__ == '__main__':
    main()