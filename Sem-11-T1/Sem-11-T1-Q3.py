print('''
    03. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
        número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos
        (excluindo o zero).
        Dica: use repetição com teste no final
''')

def main():
    maior = 0
    menor = 0
    
    while True:
        n = int(input('Digite um numero inteiro ou digite [0] para encerrar: '))
        
        if n == 0:
            break
        
        if menor == 0:
            menor = n
            
        if n < menor:
            menor = n
        
        if n > maior:
            maior = n

    print(f'O maior numero digitado é: {maior}')
    print(f'O menor numero digitado é: {menor}')

if __name__ == '__main__':
    main()
