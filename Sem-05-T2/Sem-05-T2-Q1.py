'''01. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma VOGAL ou o
valor booleano False (falso) caso contrário.'''

def valida (caractere):
    valor = caractere.lower() in 'aeiou'
    return valor

def main():
    print('Vamos saber se o caractere digitado é uma VOGAL?')
    entrada_caracatere = input('digite o caractere desejado: ').strip()
    
    resultado = valida(entrada_caracatere)
    
    print(f'\nO caractere digitado é: {resultado}')
    print('Obs: True = Verdadeiro e False = Falso')
    
if __name__ == '__main__':
    main()