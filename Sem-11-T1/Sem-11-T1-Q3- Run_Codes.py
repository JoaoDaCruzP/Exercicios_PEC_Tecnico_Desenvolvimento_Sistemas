'''
    03. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
        número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos
        (excluindo o zero).
        Dica: use repetição com teste no final
'''

def main():
    maior = 0
    menor = 0
    
    while True:
        n = int(input())
        
        if n == 0:
            break
        
        if menor == 0:
            menor = n
            
        if n < menor:
            menor = n
        
        if n > maior:
            maior = n

    print(maior)
    print(menor)

if __name__ == '__main__':
    main()
