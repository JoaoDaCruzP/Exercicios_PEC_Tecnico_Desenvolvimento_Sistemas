'''
    05. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    a) "Telefonou para a vítima?"
    b) "Esteve no local do crime?"
    c) "Mora perto da vítima?"

    d) "Devia para a vítima?"
    e) "Já trabalhou com a vítima?"

    Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa
    no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4
    como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

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
        
    i_a = input().upper()
    i_b = input().upper()
    i_c = input().upper()
    i_d = input().upper()
    i_e = input().upper()

    analise = desvenda_crime(i_a,i_b,i_c,i_d,i_e)

    if analise == 2:
        resultado = 'Suspeito'
    elif 3 <= analise <= 4:
        resultado = 'Cúmplice'
    elif analise == 5:
        resultado = 'Assassino'
    else:
        resultado = 'Inocente'


    print(resultado)
    
if __name__ == '__main__':
    main()