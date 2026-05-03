from random import randint

print('''

                   BEM VINDO AO JOGO "21"
   =================================================== 
      O objetivo do jogo é somar numeros a cada rodada 
              até o resultado chegar a 21

''')

def main():

    soma = 0
    jogando = True

    print(10 * '*' + 'Vamos jogar 21' + 10 * '*')
    escolha_jogar = input('\nEsta preparado? [s]sim [n]nao: ').strip() #entrada do usuario
    if escolha_jogar[0].lower() == 'n':
        print('Lamentamos, Aposto que iria se divertir bastante')
    
    else:

        #looping que executa enquanto a pontuação do jogador não chegar a 3!
        while jogando == True:

            carta = randint(1,10) #seleciona o numero da rodada
            print(10 * '=')
            print(f'A carta revelada é: {carta}')
            print(10 * '=')
            
            escolha_somar = input(f'Deseja ficar com a carta?[s]sim [n]nao: ').strip()
            
            if escolha_somar[0] == 's':
                soma += carta
            
            print(f'A soma das cartas é: {soma}')

            if soma == 21:
                print('Parabens!!\n')
                jogando = False
            
            elif soma > 21:
                print('Você perdeu!!\n')
                jogando = False
                

    print('=' * 30)
    print('Obrigado por Jogar!!')
    print(f'A soma das cartas deu: {soma}') #Imprime o numero de tentativas
    print('=' * 30)
    print('deixe seu feedback: joaodesenvolvedor@gmail.com') 

if __name__ == '__main__':
    main()