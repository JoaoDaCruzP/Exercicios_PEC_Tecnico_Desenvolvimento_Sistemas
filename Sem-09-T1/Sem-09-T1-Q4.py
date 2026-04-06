print('''
    04. Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui
    menor diferença com relação ao primeiro, imprimindo o valor da diferença.
''')

def verifica_numero(n1,n2,n3):

    if n1 > n2:
        dif1 = n1 - n2
    else:
        dif1 = n2 - n1

    if n3 > n1:
        dif2 = n3 - n1
    else:

        return n1 - n3
    
    if dif1 < dif2:
        return dif1, f'O segundo numero possui menor diferença'
    else:
        return dif2, f'O terceiro numero possui menor diferença'
    
def main():

    i_num1 = int(input('Digite um numero inteiro: '))
    i_num2 = int(input('Digite outro numero inteiro: '))
    i_num3 = int(input('Digite mais um numero inteiro: '))
    

    resultado, diferenca = verifica_numero(i_num1,i_num2,i_num3)

    print(f'{diferenca} que é de: {resultado}')
if __name__ == '__main__':
    main()