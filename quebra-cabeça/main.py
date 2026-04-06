#IMPORTAÇÃO DAS BIBLIOTECAS
import urllib.request
from unicodedata import normalize

#SEPARA DA DATA DIGITADA EM DIA, MES ANO
def separar_data(dma):
    a = dma % 10000
    dma //= 10000

    m = dma % 100
    dma //= 100

    d = dma

    return d, m, a

#ATRIBUI UM SIGNO CORRESPONDENTE À DATA DIGITADA PELO USUARIO
def signo(dia,mes):

    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    if mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    if mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    if mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    if mes == 7:
        return 'Câncer' if dia < 23 else 'Leão'
    if mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'        
    if mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    if mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    if mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    if mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricornio'
    if mes == 1:
        return 'Capricornio' if dia < 20 else 'Aquário'
    if mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

#FUNÇÃO CRIADA PARA REMOVE OS ACENTOS DE UMA PALAVRA
def remover_acentos(texto):
    return normalize('NFKD', texto).encode('ASCII','ignore').decode('ASCII')

#FAZ UMA CONSULTA EM UM SITE FORNECIDO, BUSCANDO UMA TAG HTML ESPECIFICA E RETORNA OS DADOS DA CONSULTA
def horoscopo(signo_desejado):

    #RECEBE E TRATA O PARAMETRO SIGNO QUE SERÁ PASSADO PELA FUNÇÃO SIGNO
    signo_formatado = remover_acentos(signo_desejado).lower()

    #VARIAVEL QUE RECEBE O ENDEREÇO DO SITE DE CONSULTA SINO
    minha_url = 'https://www.horoscopovirtual.com.br/horoscopo/'+ signo_formatado #BUSCA COM SUFIXO DO SIGNO DESEJADO

    # AQUI EU NÃO SEI EXPLICAR 100%, MAS SEI QUE ESTA PEDINDO OS DADOS PRO SITE E TRATANDO ESSES DADOS PARA NAO DAR ERRO
    requisicao = urllib.request.Request(
        url= minha_url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    # RECEBE A RESPOSTA DA URL
    resposta = urllib.request.urlopen(requisicao)

    # QUARDA OS DADOS COM ACENTO COM O DECODE UTF-8
    pagina = resposta.read().decode('utf-8')

    #NESSE TRECHO EU FIZ ALGUMAS MODIFICAÇÕES PARA TRAZER APENAS O RESOLTAD ESPERADO!
    #OBS: ESTAVA QUEBRANDO POR NAO ENCONTRAR A TAG QUE FOI ENTREGUE NO EXERCICIO

    #DEFINE QUAL A TAG QUE SERA LIDA E ARMAZENADA
    marcador_inicio = pagina.find('class="text-wrapper"')

    #ENCONTRA DENTRO DA DIV TEXT-WRAPPER O PARAGRAFO QUE SERA MOSTRADO NA TELA
    marcardor_tag = pagina.find('<p>', marcador_inicio)

    #DEFINE ONDE ACABA O PARAGRAFO PARA PODER MOSTRAR SO O LIMIE DO PARAGRAFO
    marcador_final = '</p>'

    inicio = marcardor_tag
    final = pagina.find(marcador_final, inicio)

    # RETIRA DA STRING QUE SERA MOSTRADA A TAG DE INICIO E FECHAMENTO
    resultado_limpo = pagina[inicio:final].replace('<p>','')

    #FINALMENTE RETORNA O RESULTADO QUE É O HOROSCOPO DO DIA PARA O SIGNO CORRESPONDENTE A DATA DIGITADA PELO USUARIO
    return f' O horoscopo do dia para ' + signo_desejado + ' é: ' + resultado_limpo

def main():

    entrada_nascimento = int(input('Digite sua data de nascimento no formato DDMMAAAA: '))

    #CHAMA A FUNÇÃO PRA SEPARAR  A DATA
    dia, mes, _ = separar_data(entrada_nascimento) 
    
    # USA O DIA E O MES SEPARADO PARA ENCONTRAR O SIGNO
    meu_signo = signo(dia, mes)
    
    # RECEBE O RESULTADO DO HOROSCOPO DO DIA DO SIGNO DEFINIDO E ARMARZENA NA VARIAVEL
    horoscopo_de_hoje = horoscopo(meu_signo)

    # MOSTRA O RESULTADO PARA O USUARIO
    print(horoscopo_de_hoje)

if __name__=='__main__':
    main()