print(
    '''
    04. Escreva um programa que gere a seguinte sequência:
    10, 20, 30, 40, ..., 990, 1000.

    Considere a separação dos números por vírgula seguido de espaço em branco e o ponto no final da
    sequência.
    ''')

def main():
    num = 0
    valores = ''

    for i in range(100):
        num += 10

        if num < 1000:
            valores += f'{num}, '
        
        else:
            valores += f'{num}.'


    print(valores)

if __name__ == '__main__':
    main()