'''
    01. Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja
    ímpar. Mostre na tela o resultado da operação.
'''

def par_impar(numero):
    if numero % 2 == 0:
        return numero + 5
    
    else:
        return numero + 8
        
def main():

    i_numero = int(input())

    resultado = par_impar(i_numero)

    print(resultado)

if __name__ == '__main__':
    main()