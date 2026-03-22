print('''
05. Escreva um programa que leia três números correspondentes a três notas de um aluno. Apresente a média das três
notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média
final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.
''')

def calcula_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    
    if n3 > 8:
        media += 1
        
    if media > 10:
        media = 10

    return media

def main():
    entrada_nota1 = float(input('Nota 01: '))
    entrada_nota2 = float(input('Nota 02: '))
    entrada_nota3 = float(input('Nota 03: '))
    
    resultado = calcula_media(entrada_nota1,entrada_nota2,entrada_nota3)

    print(f'O resultado da média é: {resultado:.2f}')
    
if __name__ == '__main__':
    main()
    