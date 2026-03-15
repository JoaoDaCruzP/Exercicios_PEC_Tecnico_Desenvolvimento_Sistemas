'''
01. Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! Vamos fazer um contador
de letras. Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa
frase sem considerar espaços em branco no início ou final da frase digitada.
'''

def conta_frase(frase):
    valor = len(frase)
    return valor

def main():
    print('CONTADOR DE CARACTERES DE UMA FRASE\n')
    entrada_frase = input('Digite uma frase: ').strip()
    
    resultado = conta_frase(entrada_frase)
    print(f'\nSua frase possui: {resultado} caracteres')
    
if __name__ == '__main__':
    main()