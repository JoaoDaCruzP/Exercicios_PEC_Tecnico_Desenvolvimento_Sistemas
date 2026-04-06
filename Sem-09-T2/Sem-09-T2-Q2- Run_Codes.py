'''
    02. Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas,
    dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores
    e o ponto “.” no final da frase. Exemplos:

    • 521 = cinco centenas, duas dezenas e uma unidade.
    • 107 = uma centena e sete unidades.
    • 80 = oito dezenas.
'''
def verifica_numero(n1):

    if n1 > 1000:
        raise ValueError('numero maior que mil')
    
    else:
        centena = n1 // 100
        dezena = (n1 % 100) // 10
        unidade = n1 % 10

    return centena,dezena,unidade
    
def main():

    i_num1 = int(input())
    
    centena,dezena,unidade = verifica_numero(i_num1)

    f_centena = ''
    f_dezena = ''
    f_unidade = ''

    if centena == 1:
        f_centena = 'uma centena'
    elif centena == 2:
        f_centena = 'duas centenas'
    elif centena == 3:
        f_centena = 'três centenas'
    elif centena == 4:
        f_centena = 'quatro centenas'
    elif centena == 5:
        f_centena = 'cinco centenas'
    elif centena == 6:
        f_centena = 'seis centenas'
    elif centena == 7:
        f_centena = 'sete centenas'
    elif centena == 8:
        f_centena = 'oito centenas'
    elif centena == 9:
        f_centena = 'nove centenas'

    if dezena == 1:
        f_dezena = 'uma dezena'
    elif dezena == 2:
        f_dezena = 'duas dezenas'
    elif dezena == 3:
        f_dezena = 'três dezenas'
    elif dezena == 4:
        f_dezena = 'quatro dezenas'
    elif dezena == 5:
        f_dezena = 'cinco dezenas'
    elif dezena == 6:
        f_dezena = 'seis dezenas'
    elif dezena == 7:
        f_dezena = 'sete dezenas'
    elif dezena == 8:
        f_dezena = 'oito dezenas'
    elif dezena == 9:
        f_dezena = 'nove dezenas'

    if unidade == 1:
        f_unidade = 'uma unidade'
    elif unidade == 2:
        f_unidade = 'duas unidades'
    elif unidade == 3:
        f_unidade = 'três unidades'
    elif unidade == 4:
        f_unidade = 'quatro unidades'
    elif unidade == 5:
        f_unidade = 'cinco unidades'
    elif unidade == 6:
        f_unidade = 'seis unidades'
    elif unidade == 7:
        f_unidade = 'sete unidades'
    elif unidade == 8:
        f_unidade = 'oito unidades'
    elif unidade == 9:
        f_unidade = 'nove unidades'


    contador = 0
    if centena != 0:
        contador +=1
    if dezena != 0:
        contador +=1
    if unidade != 0:
        contador +=1


    if centena == 0 and contador == 2:
        print(f'{f_dezena} e {f_unidade}.')
    
    elif dezena == 0 and contador == 2:
        print(f'{f_centena} e {f_unidade}.')

    elif unidade == 0 and contador == 2:
        print(f'{f_centena} e {f_dezena}.')


    if (centena == 0 and contador == 1) and (dezena == 0 and contador == 1):
        print(f'{f_unidade}.')
    
    elif (unidade == 0 and contador == 1) and (centena == 0 and contador == 1):
        print(f'{f_dezena}.')
        
    elif (dezena == 0 and contador == 1) and (unidade == 0 and contador == 1) :
        print(f'{f_centena}.')
        
    if contador == 3:
        print(f'{f_centena}, {f_dezena} e {f_unidade}.')

if __name__ == '__main__':
    main()