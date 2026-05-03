'''
    01. Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação:
        A condição de saída do laço será a leitura do valor 0 (flag).
'''
def main():
    soma = 0

    while True:
        n = int(input())

        if n == 0:
            break
        soma += n
    
    print(soma)

if __name__ == '__main__':
    main()

