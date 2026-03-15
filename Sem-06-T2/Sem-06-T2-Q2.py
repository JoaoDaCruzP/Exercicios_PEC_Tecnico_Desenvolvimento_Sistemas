'''
02. Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso!
Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro
mais próximo e imprima o resultado.
'''

def arrendonda(valor):
    arredondado = round(valor)
    return arredondado

def main():
    print('VAMOS ARRENDONDAR O VALOR DIGITADO\n')
    entrada_valor = float(input('Digite um valor: ').strip())
    
    resultado = arrendonda(entrada_valor)
    
    print(f'\nO valor digitado arrendodado é: {resultado}')
    
if __name__ == '__main__':
    main()