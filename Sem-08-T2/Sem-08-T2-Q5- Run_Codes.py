'''
    05. Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas
    obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:

    Média Final = Nota 1 + Nota 2 ∗ 2 + Nota 3 ∗ 3 + Média Exercícios / 7

    A atribuição dos conceitos obedece a tabela abaixo.

    Conceito Média Final
    A >= 9.0
    B >= 7.5 e < 9.0
    C >= 6.0 e < 7.5
    D >= 4.0 e < 6.0
    E < 4.0

    O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado”
    se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.
'''

def calculo_media(n1,n2,n3,m_ex):
    media_final = (n1 + (n2 * 2) + (n3 * 3) + m_ex) / 7

    if media_final >= 9:
        return media_final, 'A', 'Aprovado'
    elif 7.5 <= media_final < 9.0:
        return media_final, 'B', 'Aprovado'
    elif 6.0 <= media_final < 7.5:
        return media_final, 'C', 'Aprovado'
    elif 4.0 <= media_final < 6.0:
        return media_final, 'D', 'Reprovado'
    else:
        return media_final, 'E', 'Reprovado'

def main():
    matricula = input()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media_exercicios = float(input())

    media_final,conceito,resultado = calculo_media(nota1,nota2,nota3,media_exercicios)
    
    print(matricula)
    print(f'{media_final:.2f}')
    print(conceito)
    print(resultado)
    

if __name__ == '__main__':
    main()
