'''
    02. Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou
    o valor booleano False (falso) caso contrário.
'''

def  e_booleano(num):
    return not num % 2 == 0 

def main():
    entrada_num = int(input().strip())
    
    resultado = e_booleano(entrada_num)
    
    print(resultado)
    
if __name__ == '__main__':
    main()

