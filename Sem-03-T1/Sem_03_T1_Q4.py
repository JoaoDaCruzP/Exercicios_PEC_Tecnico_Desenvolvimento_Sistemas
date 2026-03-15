'''04. O tempo é algo legal, especialmente quando você vai calcular quantos minutos há em um número específico de
segundos. Peça ao usuário para inserir um número de segundos. Em seguida, use a divisão inteira para mostrar esse
tempo em minutos (lembre-se, 1 minuto = 60 segundos) e use o resto da divisão inteira para saber quantos segundos
sobram. Imprima os resultados.'''

entrada_seg = int(input('Digite quantos segundos: ').strip())
minutos = entrada_seg // 60
seg = entrada_seg % 60

print(f'O valor digitado é igual a {minutos} minutos e {seg} segundos')
