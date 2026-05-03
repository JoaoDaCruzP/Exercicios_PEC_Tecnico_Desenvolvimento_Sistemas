from turtle import *


'''                     Dicionario de comandos:

shape = formato da caneta                       speed = velocidade
color = cor da caneta                           backward = retroce
forward = avança                                left = vira pra esquerda
right = vira pra direita                        pendown = baixa a caneta e deixa rastro
penup = levanta a canet e nao deixa rastros

'''
def desenha_quadrado():

    #desenhando um quadrado
    pendown()
    for i in range(4):
        forward(200)
        right(90)
    clear() #apaga o desenho

def desenha_triangulo():
     #desenha um triangulo
    right(60)
    for i in range(3):
        forward(200)
        right(120)

    reset() #reseta o programa
    penup()

def desenha_casa():
    #desenha o telhado
    for i in range(2):
        forward(200)
        right(45)
        forward(150)
        right(135)
    right(135)
    forward(150)

    #desenha frente
    left(135)
    forward(20)
    left(90)
    forward(20)
    right(180)
    forward(120)
    left(90)
    forward(180)
    left(90)
    forward(110)

    #desenha porta e janela da frente
    penup()

    #posição da porta
    backward(110)
    right(90)
    backward(160)
    left(90)

    #desenha porta
    pendown()
    color('brown')
    for i in range(2):
        forward(100)
        right(90)
        forward(50)
        right(90)

    #posição da janela
    penup()
    right(90)
    forward(80)
    left(90)
    forward(100)
    right(90)
    forward(60)

    #desenha a janela
    pendown()
    for i in range(2):
        right(90)
        forward(60)
        right(90)
        forward(60)

    # desenha lateral

    #posição da parede
    penup()
    right(90)
    forward(100)
    left(90)

    #desenha parede
    color('black')
    pendown()
    forward(200)
    left(90)
    forward(100)

    #pinta o telhado
    penup()
    #posicao inicial do telhado
    forward(2)
    right(90)
    forward(28)

    #pintando telhado
    color('red')
    pendown()
    left(135)

    speed(11)
    for i in range(33):
        forward(145)
        left(45)
        forward(3)
        left(135)
        forward(145)
        right(135)
        forward(3)
        right(45)

def main():

    #definições iniciais
    shape('arrow') 
    speed(2) 
    color('blue')

    #define o inicio do desenho
    penup()
    left(90)
    forward(100)
    right(90)
        
    desenha_quadrado()
    desenha_triangulo()

    #posição inicial do desenho
    backward(100) 
    left(90) 
    forward(100)
    right(90)
    pendown()
    speed(2)

    desenha_casa()
    
    done()
if __name__ == "__main__":
    main()
