print('''
    02. Escreva um programa que, para um número indeterminado de pessoas:

        a. leia a idade de cada pessoa, sendo que a leitura da idade 0 (zero) indica o fim dos dados (flag)
        e não deve ser considerada;
        b. calcule e escreva o número de pessoas;
        c. calcule e escreva a idade média do grupo;
        d. calcule e escreva a menor idade e a maior idade.
''')

def main():
    n_pessoas = 0
    idade_media = 0
    menor = 0
    maior = 0

    while True:
        idade = int(input('Digite sua idade: '))

        if idade == 0:
            break

        n_pessoas += 1
        idade_media += idade

        if idade > maior:
            maior = idade

        if menor == 0:
            menor = idade
        
        if idade < menor:
            menor = idade
        

    idade_media = idade_media / n_pessoas

    print(f'numero de pessoas: {n_pessoas}')
    print(f'media das idades: {idade_media}')
    print(f'maior idade: {maior} e menor idade: {menor}')
        

if __name__ == '__main__':
    main()