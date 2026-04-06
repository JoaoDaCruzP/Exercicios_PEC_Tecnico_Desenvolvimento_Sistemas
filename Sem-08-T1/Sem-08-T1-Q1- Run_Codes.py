'''
    01. Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de  
    nascimento de uma pessoa, calcule e escreva a idade exata em anos
'''
def calcula_idade(a_nascimento,a_atual):
    return a_atual - a_nascimento


dia_atual = int(input())
mes_atual = int(input())
ano_atual = int(input())

dia_nasc = int(input())
mes_nasc = int(input())
ano_nasc = int(input())



idade = calcula_idade(ano_nasc,ano_atual)

def verifica_idade_exata():
    #verifica se 
    if mes_nasc > mes_atual:
        return idade - 1
    
    elif mes_nasc < mes_atual:
        return idade
    
    elif mes_nasc == mes_atual:
        if dia_atual >= dia_nasc:
            return idade
        else:
            return idade - 1
    
    else:
        raise ValueError('O valor digitado so pode ser numeros')
        
def main():

    idade_exata = verifica_idade_exata()
    print(idade_exata)

if __name__ == '__main__':
    main()