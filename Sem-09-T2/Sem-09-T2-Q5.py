print('''
    05. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a) "Telefonou para a vítima?"
    b) "Esteve no local do crime?"
    c) "Mora perto da vítima?"

    d) "Devia para a vítima?"
    e) "Já trabalhou com a vítima?"

    Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa
    no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4
    como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
''')

def desvenda_crime(a,b,c,d,e):
    contador = 0
    if a[0] == 'S':
        contador += 1
    if b[0] == 'S':
        contador += 1
    if c[0] == 'S':
        contador += 1
    if d[0] == 'S':
        contador += 1
    if e[0] == 'S':
        contador += 1

    return contador

def main():
    print('Interrogatório Iniciado!\n')
    i_a = input('a) "Telefonou para a vítima?": ').upper()
    i_b = input('b) "Esteve no local do crime?": ').upper()
    i_c = input('c) "Mora perto da vítima?": ').upper()
    i_d = input(' d) "Devia para a vítima?": ').upper()
    i_e = input('e) "Já trabalhou com a vítima?": ').upper()

    analise = desvenda_crime(i_a,i_b,i_c,i_d,i_e)

    if analise == 2:
        resultado = 'Não deixe a cidade, nem mude de endereço vo ainda é Suspeito'
    elif 3 <= analise <= 4:
        resultado = 'você é Culpado e se enquadra como Cúmplice'
    elif analise == 5:
        resultado = 'você é Culpado e se enquadra como Assassino'
    else:
        resultado = 'você é Inocente'

    print(f'\nTotal de "sim": {analise}')
    print(f'Pelo resultado das suas respostas... {resultado}!')
    
if __name__ == '__main__':
    main()