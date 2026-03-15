'''03. A fábrica de doces precisa de ajuda para embalar os doces corretamente. Cada pacote deve conter um número
inteiro de doces. Peça ao usuário para inserir o número de doces produzidos e o número de pacotes disponíveis.
Divida os doces igualmente entre os pacotes fazendo a divisão inteira para garantir que cada pacote contém a mesma
quantidade de doces. Imprima o número de doces em cada pacote.'''

#captura a quantidade de doces
doces = int(input('Digite a quantidade de doces: ').strip())
#captura a quantidade de pacotes
pac = int(input('Digite a quantidade de pacotes: ').strip()) 

empacotados = (doces // pac) #divide sem resto o numero de doces pelo numero de pacotes

print(f'Total de pacotes: {empacotados}') #mostra na tela o resultado
