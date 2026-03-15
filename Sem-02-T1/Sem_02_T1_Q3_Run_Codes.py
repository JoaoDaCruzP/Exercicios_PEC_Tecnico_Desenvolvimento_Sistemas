'''
03. Você encontrou um poço dos desejos, mas ele só realiza desejos que envolvem matemática! Peça ao usuário para inserir o valor encontrado no poço. Agora calcule quantas moedas de R$0,25 somam o valor no poço sem ultrapassar o total encontrado.
'''

entrada_valor = float(input().strip())
        
quant_moedas_25centavos = entrada_valor // 0.25

print(f'{quant_moedas_25centavos:.0f}')