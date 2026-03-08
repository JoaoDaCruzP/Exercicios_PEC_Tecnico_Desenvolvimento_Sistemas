'''
02. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou o valor booleano False (falso) caso contrário.

'''

def verifica(caractere):
    return 'a' <= caractere.lower() <= 'z'

def main():
    print('Vamos descobrir se o caractere digitado é uma Letra?\n')
    
    entrada_caractere = input('Digite o caractere desejado: ').strip()
    
    resultado = verifica(entrada_caractere)
    
    print(f'\nO caractere digitado é: {resultado}')
    print('Obs: True = Verdadeiro e False = Falso')
    
if __name__ == '__main__':
    main()