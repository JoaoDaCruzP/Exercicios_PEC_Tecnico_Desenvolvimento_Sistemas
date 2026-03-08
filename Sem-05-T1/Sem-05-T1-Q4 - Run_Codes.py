'''Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertida
de para horas e minutos. Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos.
OBS: Mostre o resultado na forma H:M
'''
def converte_horas(min):
    h = min // 60
    return h

def converte_minutos(min):
    return min % 60

def main():
    
    entrada_minutos = int(input())
    
    resultado_horas = converte_horas(entrada_minutos)
    resultado_minutos = converte_minutos(entrada_minutos)
    
    print(f'{resultado_horas}:{resultado_minutos}') 
    
if __name__ == '__main__':
    main()