print('''
      03. Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido.
        • Nenhum dígito é ímpar.
        • Apenas um dígito é ímpar.
        • Os dois dígitos são ímpares.
      ''')
def e_impar(numero):
    n1 = numero // 10
    n2 = numero % 10
    
    if n1 % 2 == 0 and n2 % 2 == 0:
        return 'Nenhum dígito é ímpar.'    
    
    elif n1 % 2 == 0 or n2 % 2 == 0:
        return 'Apenas um dígito é ímpar.'

    else: 
        return 'Os dois dígitos são ímpares.'

    
def main():
    i_numero = int(input('Digite um numero inteiro entre 10 e 99: ').strip())
   
    resultado = e_impar(i_numero)
    
    print(f'Existe {resultado}')
    
if __name__ == '__main__':
    main()