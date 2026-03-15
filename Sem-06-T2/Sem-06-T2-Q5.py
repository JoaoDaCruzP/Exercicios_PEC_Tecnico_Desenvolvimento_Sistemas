'''
05. Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas!
Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:

°F = (°C * (9/5)) + 32
'''
def converte_celcius_p_fahrenheit(temperatura_g_c):
    temperatura_g_f = (temperatura_g_c * (9/5)) + 32 
    return temperatura_g_f

def main():
    print('VAMOS CONVERTER UMA TEMPERATURA EM Celsius(°C) PARA Fahrenheit(°F)\n')
    entrada_temperatura = float(input('Digite uma temperatura: ').strip())
    
    resultado = converte_celcius_p_fahrenheit(entrada_temperatura)
    
    print(f'{entrada_temperatura} graus Celsius(°C) é igual a {resultado:.2f} graus Fahrenheit(°F)')

if __name__ == '__main__':
    main()