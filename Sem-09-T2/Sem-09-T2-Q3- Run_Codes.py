'''
    03. Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.
    OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas;
    Considere que em anos bissextos o mês de fevereiro tem 29 dias.
'''

def valida_data(data):
    dia = data // 1000000
    mes = (data % 1000000) // 10000
    ano = data % 10000

    if mes == 1:
        if 1 <= dia <= 31:
            return True
        return False
    elif mes == 2:
        if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
            if 1 <= dia <= 29:
                return True
            return False
        else:
            if 1 <= dia <= 28:
                return True
            return False
    elif mes == 3:
        if 1 <= dia <= 31:
            return True
        return False
    elif mes == 4:
        if 1 <= dia <= 30:
            return True
        return False
    elif mes == 5:
        if 1 <= dia <= 31:
            return True
        return False
    elif mes == 6:
        if 1 <= dia <= 30:
            return True
        return False
    elif mes == 7:
        if 1 <= dia <= 31:
            return True
        return False
    elif mes == 8:
        if 1 <= dia <= 31:
            return True
        return False
    elif mes == 9:
        if 1 <= dia <= 30:
            return True
        return False
    elif mes == 10:
        if 1 <= dia <= 31:
            return True
        return False
    elif mes == 11:
        if 1 <= dia <= 30:
            return True
        return False
    elif mes == 12:
        if 1 <= dia <= 31:
            return True
        return False
    else:
        return False

def main():
    i_data = int(input())
    resultado = valida_data(i_data)
    print(resultado)

if __name__ == '__main__':
    main()