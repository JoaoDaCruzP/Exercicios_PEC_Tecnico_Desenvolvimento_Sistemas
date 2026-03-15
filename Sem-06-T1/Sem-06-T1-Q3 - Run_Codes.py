''' 03. Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse
tempo em horas, minutos e segundos (HH:MM:SS).

'''
'''
def horas(seg):
    h = seg // 3600
    return h

def minutos(seg):
    m = (seg % 3600) // 60
    return m
    
def segundos(seg):
    s = seg % 60
    return s
'''
    
   
def converte_h_m_s(seg):
    h = seg // 3600
    m = (seg % 3600) // 60
    s = seg % 60
    return h,m,s   
    
def main():
    entrada_seg = int(input().strip())
    '''
    resutado_h = horas(entrada_seg)
    result_m = minutos(entrada_seg)
    result_s = segundos(entrada_seg)
    '''
    
    result_h,result_m,result_s = converte_h_m_s(entrada_seg)
    
    print(f'{result_h}:{result_m}:{result_s}')
    
if __name__ == '__main__':
    main()