'''
    02. Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual
    delas é a mais recente.
'''
def verifica_idade(dia,mes,ano,dia_atual,mes_atual,ano_atual):

    if ano_atual > ano:
        #print('etapa 1')
        return dia_atual,mes_atual, ano_atual
    
    elif ano_atual < ano:
        #print('etapa 2')
        return dia,mes,ano
    
    elif ano_atual == ano:
        #print('etapa 3')
        if mes_atual < mes:
            #print('etapa 3/1')
            return dia,mes,ano
        
        elif mes_atual == mes:
            if dia_atual > dia:

                #print('etapa 3/2')
                return dia_atual,mes_atual,ano_atual
            else:
                #print('etapa 3/3')
                return dia,mes,ano
            
        else:
            #print('etapa 3/4')
            return dia_atual,mes_atual,ano_atual
    else:
        #print('etapa 4')
        raise ValueError('Digite uma data valida')


def main():

    dia = int(input().strip())
    mes = int(input().strip())
    ano = int(input().strip())

    d_atual = int(input().strip())
    m_atual = int(input().strip())
    a_atual = int(input().strip())
   
    dia_mais_recente,mes_mais_recente,ano_mais_recente = verifica_idade(dia,mes,ano,d_atual,m_atual,a_atual)

    print(f'{dia_mais_recente}/{mes_mais_recente}/{ano_mais_recente}')

if __name__ == '__main__':
    main()