from random import randint

print('''

                   Porta da fortuna 
   ===================================================
     Existe um prêmio atrás de uma das portas abaixo,
     Advinhe qual a porta certa para ganhar o prêmio
      
         _______        _______           _______
        |       |      |       |         |       |
        |       |      |       |         |       |
        |  [1]  |      |  [2]  |         |  [3]  |
        |       |      |       |         |       |
        |_______|      |_______|         |_______|
      
          Escolha entre as portas [1]  [2] ou [3]:
''')

def main():


    pontuacao = 0
    rodada = 0

    jogando = True

    #looping que executa enquanto a resposta do jogador for 'n'
    while jogando == True:

        rodada += 1 #conta o numero de rodadas
        print( 10 * '=' + f'Rodada {rodada}' + '=' * 10)

        escolha = int(input('Digite o numero da porta: ')) #entrada do usuario ja convertida pra numero inteiro
        
        porta_certa = randint(1,3) #seleciona a porta sorteada
        
        print(f'Você escolheu a porta: {escolha}')
        print(f'A porta certa é a: {porta_certa}')

        #lógica que verifica a resposta do usuario
        if escolha == porta_certa:
            print('Parabens!!')
            pontuacao += 1
        else:
            print('Que pena')
            pontuacao = 0  #zera a pontuação se o usuario errar a resposta

        #condição que encerra o looping se a resposta do usuario for 'n'
        resposta = input('Deseja continuar o jogo? [n]não ou [s]sim: ').strip()
        if resposta[0].lower() == 'n':
            jogando = False
        
    print('=' * 30)
    print('Obrigado por Jogar!!')
    print(f'Sua pontuanção final foi: {pontuacao} de {rodada}') #Imprime a pontuação e o numero de rodadas jogadas
    print('=' * 30)
    print('deixe seu feedback: joaodesenvolvedor@gmail.com') 

if __name__ == '__main__':
    main()