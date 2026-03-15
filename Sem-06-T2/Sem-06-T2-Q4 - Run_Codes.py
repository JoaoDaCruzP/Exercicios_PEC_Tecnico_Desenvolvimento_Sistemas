'''
04. Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.
'''
def anos_terreste_p_anos_espaciais(idade):
    valor = idade / 2
    return valor

def main():
    entrada_idade = int(input().strip())
    
    resultado = anos_terreste_p_anos_espaciais(entrada_idade)
    print(int(resultado))
    
if __name__ == '__main__':
    main()