'''
03. Você encontrou um poço dos desejos, mas ele só realiza desejos que envolvem matemática! Peça ao usuário para inserir o valor encontrado no poço. Agora calcule quantas moedas de R$0,25 somam o valor no poço sem ultrapassar o total encontrado.
'''

print('03. Você encontrou um poço dos desejos, mas ele só realiza desejos que envolvem matemática! Peça ao usuário para inserir o valor encontrado no poço. Agora calcule quantas moedas de R$0,25 somam o valor no poço sem ultrapassar o total encontrado.')

entrada_valor = float(input('Digite a quantidade encotrada no poço: ').strip())
        
quant_moedas_25centavos = entrada_valor // 0.25

print(f'A quantidade de moedas de R$0,25 centavos é: {quant_moedas_25centavos}')