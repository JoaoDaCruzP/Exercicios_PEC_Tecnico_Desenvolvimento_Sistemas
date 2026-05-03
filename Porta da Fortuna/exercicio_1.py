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

    #laço de repetição 
    for i in range(3):

        rodada += 1 #conta o numero de rodadas
        print( 10 * '=' + f'Rodada {rodada}' + '=' * 10) 

        escolha = int(input('Digite o numero da porta: ')) #entrada do usuario ja convertida pra numero inteiro
        
        porta_certa = randint(1,3) # porta sorteada
        
        print(f'Você escolheu a porta: {escolha}')
        print(f'A porta certa é a: {porta_certa}')

        #condição que verifica a resposta do usuario
        if escolha == porta_certa:
            print('Parabens!!')
            pontuacao += 1
        else:
            print('Que pena')

    
    print('=' * 30)
    print(f'Sua pontuanção final foi: {pontuacao}')
    print('=' * 30)
    
if __name__ == '__main__':
    main()