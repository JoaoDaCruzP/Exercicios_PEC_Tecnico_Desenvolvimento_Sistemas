'''
  05. Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.
'''

def main():

    maior = 0
    for i in range(100):

        num = int(input())
        if num > maior:
            maior = num
    
    print(maior)

if __name__ == '__main__':
    main()