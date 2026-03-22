'''
    02. Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.
'''

def digitos_pares(numero):

    n1 = numero // 100
    n2 = (numero // 10) % 10
    n3 = numero % 10 
    return n1,n2,n3
         
def main():
    contador = 0
    i_numero = int(input().strip())
    
    n1,n2,n3 = digitos_pares(i_numero)
    
    if n1 % 2 == 0 and i_numero > 100:
        contador += 1
        
    if n2 % 2 == 0:
        contador +=1
        
    if n3 % 2 == 0:
        contador += 1

    print(f'{contador}')
    
if __name__ == '__main__':
    main()