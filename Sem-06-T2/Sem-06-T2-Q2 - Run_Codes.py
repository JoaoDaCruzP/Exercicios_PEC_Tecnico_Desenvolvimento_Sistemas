'''
02. Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso!
Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro
mais próximo e imprima o resultado.
'''

def arrendonda(valor):
    arredondado = round(valor)
    return arredondado

def main():
    entrada_valor = float(input().strip())
    
    resultado = arrendonda(entrada_valor)
    
    print(f'{resultado}')
    
if __name__ == '__main__':
    main()