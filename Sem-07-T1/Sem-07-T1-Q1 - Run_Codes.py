'''
    01. Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo
    Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro
    1 para identificar masculino e 2 para identificar feminino.
'''

def saudacao (nome,sexo):
    if sexo == 1: 
        return f'Ilmo Sr. {nome}'
    else:
        return f'Ilma Sra. {nome}'

def main():
    
    entrada_nome = input().strip()
    entrada_sexo = int(input().strip())
    
    resultado = saudacao(entrada_nome, entrada_sexo)
    
    print(resultado)
    
if __name__ == '__main__':
    main()