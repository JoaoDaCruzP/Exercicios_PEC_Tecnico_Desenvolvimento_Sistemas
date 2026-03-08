'''
04. Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal ou consoante) ou um NÚMERO (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.
'''
def verifica(caractere):
    return caractere.lower() in '0123456789' or 'a' <= caractere.lower() <= 'z'

def main():
    print('Vamos descobrir se o caractere digitado é um numero ou uma letra?')
    print('Caso seja numero ou letra o resultado será True (verdadeiro)\n')
    entrada_caractere = input('Digite o caractere desejado: ').strip()
    
    resultado = verifica(entrada_caractere)
    
    print(f'\nO caractere digitado é: {resultado}')
    print('Obs: True = Verdadeiro e False = Falso')
    
if __name__ == '__main__':
    main()