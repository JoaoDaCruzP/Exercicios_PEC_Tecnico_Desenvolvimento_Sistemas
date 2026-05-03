'''
    04. Escreva um programa que leia número inteiro qualquer e mostre na forma invertida. Por exemplo:

        Para o número lido          A saída será
                123                           321
                1895                          5981
                14960                         6941
                53698423                      32489635
'''

def main():
    num = int(input('Digite um numero inteiro: '))

    invertido = 0
    while num > 0:
        
        invertido = (invertido * 10) + (num % 10)
        num //= 10

    print(f'O numero invertido é: {invertido}')

if __name__ == '__main__':
    main()