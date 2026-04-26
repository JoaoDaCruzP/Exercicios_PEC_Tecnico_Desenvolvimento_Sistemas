'''
    02. Modifique a canção dos programadores do exercício anterior para incluir o refrão: Tecle “Ctrl+F5”.
        Termine a canção com “Vamos fazer mais um café!”.
        99 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        100 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        101 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        ...
        250 bugs no software, pegue um deles e conserte...
        Tecle “Ctrl+F5”
        Vamos fazer mais um café!
'''

def main():
    bug = 98

    for i in range(98,250):
        bug += 1
        print(f'{bug} bugs no software, pegue um deles e conserte...')
        print('Tecle "Ctrl+F5"')
        

    print('Vamos fazer mais um café!')


if __name__ == '__main__':
    main()