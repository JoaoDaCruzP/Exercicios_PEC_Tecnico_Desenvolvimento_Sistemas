'''
03. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma CONSOANTE ou o valor booleano False (falso) caso contrário.

'''

def verifica(caracter):
    return caracter.lower() in 'bcdfghjklmnpqrstvwxyz'

def main():
    print('Vamos descobrir se o caractere digitado é uma Consoante?\n')
    entrada_caractere = input('Digite o caractere desejado: ').strip()
    
    resultado = verifica(entrada_caractere)
    
    print(f'\nO caractere digitado é: {resultado}')
    print('Obs: True = Verdadeiro e False = Falso')
    
if __name__ == '__main__':
    main()