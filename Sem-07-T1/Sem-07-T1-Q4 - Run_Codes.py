'''
    04. Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou
    “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.
'''
def identificador_caracteres(caractere):
    
    if caractere[0] in 'AEIOU':
        return 'vogal'
    elif 'A' <= caractere[0] <= 'Z':
        return 'consoante'
    elif caractere[0].isdigit():
        return 'número'
    else:
        return 'símbolo'

def main():
    
    entrada_caractere = input().strip().upper()
    
    resultado = identificador_caracteres(entrada_caractere)
    print(resultado)

if __name__ == '__main__':
    main()