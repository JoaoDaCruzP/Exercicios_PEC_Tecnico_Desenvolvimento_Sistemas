print('''
    05. Faça um programa que leia a nota de um aluno, entre zero e dez. Mostre a mensagem “Nota inválida.”
        caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar
        uma nota válida, o aluno deve ver seu conceito, segundo a tabela:
            Conceito Nota
            A >= 8,5.
            B >= 7,0
            C >= 5,0
            D >= 4
            E >= 0
''')

def main():

    while True:
        nota = float(input('Digite sua nota: '))

        if nota > 10 or nota < 0:
            print('Nota inválida.')

        else:
            
            if  nota >= 8.5:
               print('A')
            elif nota >= 7.0:
               print('B')
            elif nota >= 5.0:
                print('C')
            elif nota >= 4.0:
                print('D')
            elif nota >= 0:
                print('E')
            break

if __name__ == '__main__':
    main()