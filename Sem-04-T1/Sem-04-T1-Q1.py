'''01. Considere que as variáveis “dia”, “mês” e “ano” contém os valores respectivos de uma certa data. Escreva um comando “print”
que imprima essa data no formato usado, por exemplo, “15/4/2020” ou “2/12/2004”.'''
print('convendo no formato x-xx-xxxx')
dia = int(input('Digite o dia desejado (Ex.: 10): '))
mes = int(input('Digite o mes desejado (Ex.: 12): '))
ano = int(input('Digite o ano desejado (Ex.: 2025): '))

print(f'A data solicitada foi {dia}/{mes}/{ano}')