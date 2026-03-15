'''03. A fábrica de doces precisa de ajuda para embalar os doces corretamente. Cada pacote deve conter um número
inteiro de doces. Peça ao usuário para inserir o número de doces produzidos e o número de pacotes disponíveis.
Divida os doces igualmente entre os pacotes fazendo a divisão inteira para garantir que cada pacote contém a mesma
quantidade de doces. Imprima o número de doces em cada pacote.'''

doces = int(input().strip())
pac = int(input().strip()) 

empacotados = (doces // pac)

print(empacotados)
