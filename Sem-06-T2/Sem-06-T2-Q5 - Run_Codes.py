'''
05. Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas!
Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:

°F = (°C * (9/5)) + 32
'''
def converte_celcius_p_fahrenheit(temperatura_g_c):
    temperatura_g_f = (temperatura_g_c * (9/5)) + 32 
    return temperatura_g_f

def main():
    entrada_temperatura = float(input().strip())
    
    resultado = converte_celcius_p_fahrenheit(entrada_temperatura)
    
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()