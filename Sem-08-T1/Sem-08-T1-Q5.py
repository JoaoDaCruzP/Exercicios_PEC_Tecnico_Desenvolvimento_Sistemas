'''
    05. O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso
    ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está
    em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e
    calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:

    IMC Classificação
    < 18,5 Abaixo do peso
    < 25 Peso normal
    < 30 Sobrepeso
    < 35 Obeso leve
    < 40 Obeso moderado
    >=40 Obeso mórbido
'''

def calculo_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc


def main():
    i_peso = float(input('Digite seu peso: '))
    i_altura = float(input('Digite sua altura: '))

    result_imc = calculo_imc(i_peso,i_altura)
    print('Resultado: ')
    print(f'IMC: {result_imc:.2f}')
    if result_imc < 18.5:
        print('Abaixo do peso')
    elif result_imc < 25:
        print('Peso normal')
    elif result_imc < 30:
        print('Sobrepeso')
    elif result_imc < 35:
        print('Obeso leve')
    elif result_imc < 40:
        print('Obeso moderado')
    elif result_imc >= 40:
        print('Obeso mórbido')
    else:
        raise ValueError()

if __name__ == '__main__':
    main()
