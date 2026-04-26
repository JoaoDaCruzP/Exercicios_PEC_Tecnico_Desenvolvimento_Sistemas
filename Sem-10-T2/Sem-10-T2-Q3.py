'''
    03. Modifique a canção dos programadores novamente para aumentar os bugs de 7 em 7, iniciando em 99 e
        parando em 250 ou antes.
        99 bugs no software, pegue sete deles e conserte...
        Tecle “Ctrl+F5”
        106 bugs no software, pegue sete deles e conserte...
        Tecle “Ctrl+F5”
        113 bugs no software, pegue sete deles e conserte...
        Tecle “Ctrl+F5”
        ...
        Vamos fazer mais um café!
'''

def main():
    bug = 99

    for i in range(98,250,7):
        
        print(f'{bug} bugs no software, pegue sete deles e conserte...')
        print('Tecle "Ctrl+F5"')
        bug += 7

    print('Vamos fazer mais um café!')

if __name__ == '__main__':
    main()