print('''
    04. Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para ‘homens’ e 2 para ‘mulheres’.
    Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
    • para homens: (72.7 * altura) – 58
    • para mulheres: (62.1 * altura) – 44.7
''')

def peso_ideal(altura, sexo):
    if sexo == 1:
        return (72.7 * altura) - 58
    elif sexo == 2:
        return (62.1 * altura) - 44.7

    else:
        raise ValueError('Digite somento 1 ou 2 para o sexo')


def main():

    i_altura = float(input('Digite sua altura: '))
    i_sexo = int(input('Digite seu peso: '))
    

    resultado = peso_ideal(i_altura,i_sexo)

    print(f'O seu peso ideal é: {resultado:.2f}')

if __name__ == '__main__':
    main()