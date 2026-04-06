print('''
    03. Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores
    são diferentes. NÃO use as funções embutidas min() e max().
''')

def compara_maior(n1,n2):

    maior = n1 if n1 > n2 else n2
    return maior

def compara_menor(n1,n2):

    maior = n1 if n1 < n2 else n2
    return maior
        
def main():

    i_n1 = int(input('Digite um numero inteiro: '))
    i_n2 = int(input('Digite um numero inteiro: '))
    i_n3 = int(input('Digite um numero inteiro: '))
    i_n4 = int(input('Digite um numero inteiro: '))
    i_n5 = int(input('Digite um numero inteiro: '))

    maior = compara_maior(i_n1,i_n2)
    maior = compara_maior(i_n2,i_n3)
    maior = compara_maior(i_n3,i_n4)
    maior = compara_maior(i_n3,i_n4)
    maior = compara_maior(i_n4,i_n5)

    menor = compara_menor(i_n1,i_n2)
    menor = compara_menor(i_n2,i_n3)
    menor = compara_menor(i_n3,i_n4)
    menor = compara_menor(i_n3,i_n4)
    menor = compara_menor(i_n4,i_n5)



    print(f'O maior valor digitado é: {maior}')
    print(f'O menor valor digitado é: {menor}')

if __name__ == '__main__':
    main()