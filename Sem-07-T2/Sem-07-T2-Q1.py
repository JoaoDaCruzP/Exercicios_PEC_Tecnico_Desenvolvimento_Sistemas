print('''
      01. Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).
      ''')

def verifica_estado_civil(nome, estado_civil):
    if estado_civil == 1:
        conjuge = input('Nome do conjuge: ').strip()
        
        return len(nome) + len(conjuge)
    
    else:
        return len(nome)
    

def main():
    i_nome = input('Nome: ').strip()
    i_estado_civil = int(input('Estado civil (1-casado; 2-solteiro): ').strip())
    
    resultado = verifica_estado_civil(i_nome,i_estado_civil)
    print(f'O numero de caracateres existentes é: {resultado}')
    
if __name__ == '__main__':
    main()