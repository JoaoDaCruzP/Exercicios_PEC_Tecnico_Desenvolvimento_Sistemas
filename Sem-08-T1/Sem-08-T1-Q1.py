print('''
    01. Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de  
    nascimento de uma pessoa, calcule e escreva a idade exata em anos
''')

def calcula_idade(a_nascimento,a_atual):
    return a_atual - a_nascimento


dia_atual = int(input('Digite o dia de hoje: '))
mes_atual = int(input('Digite o mes atual: '))
ano_atual = int(input('Digite o ano atual: '))

dia_nasc = int(input('Digite seu dia de nascimento: '))
mes_nasc = int(input('Digite seu mes de nascimento: '))
ano_nasc = int(input('Digite seu ano de nascimento: '))



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
    print(f'Você tem: {idade_exata} anos')

if __name__ == '__main__':
    main()