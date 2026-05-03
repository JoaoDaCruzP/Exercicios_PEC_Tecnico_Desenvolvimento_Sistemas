print('''
    02. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
        número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos
        (excluindo o zero).
        Dica: use repetição com teste no final
''')

def main():
    soma = 0
    contador = 0

    while True:
        n = int(input('Digite um numero inteiro ou digite [0] para encerrar: '))
        
        soma += n
        
        if n == 0:
            break
        
        contador += 1
    
    media = soma / contador

    print(f'A média dos numeros digitados é: {media:.2f}')

if __name__ == '__main__':
    main()