'''
    03. Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores
    são diferentes. NÃO use as funções embutidas min() e max().
'''
def compara_menor_maior(n1,n2,n3,n4,n5):
    variavel = f'{n1}{n2}{n3}{n4}{n5}'
    return sorted(variavel)

        
def main():

    i_n1 = int(input())
    i_n2 = int(input())
    i_n3 = int(input())
    i_n4 = int(input())
    i_n5 = int(input())

    resultado = compara_menor_maior(i_n1,i_n2,i_n3,i_n4,i_n5)
    maior = resultado[4]
    menor = resultado[0]
    print(maior)
    print(menor)

if __name__ == '__main__':
    main()