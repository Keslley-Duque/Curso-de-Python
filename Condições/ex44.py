p = float(input('Digite o preço das Compras: '))
print('\nPromoção!!!\nDependendo do seu método de pagamento você pode ganhar desconto!')
print('1 - À vista em dinheiro ou cheque: 10% de desconto.\n2 - À vista no cartão: 5% de desconto.')
print('3 - Em até 2 vezes sem juros no cartão.\n4 - Em até 3 vezes ou mais no cartão: 20% de juros.')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    o = int(input('\nEscolha sua forma de pagamento.\n1 - Dinheiro \n2 - Cheque \nSua opção: '))
    if o == 1:
        print(f'\nVocê Escolheu pagar a vista em DINHEIRO! \nValor do produto: {p} Reais\nValor a ser pago à vista: {p - (p * 0.1)} Reais')
    elif o == 2:
        print(f'\nVocê Escolheu pagar a vista em CHEQUE! \nValor do produto: {p} Reais\nValor a ser pago à vista: {p - (p * 0.1)} Reais')    
elif opcao == 2:
    print(f'\nVocê Escolheu pagar à vista no cartão! \nValor do produto: {p} Reais\nValor a ser pago : {p - (p * 0.05)} Reais')
elif opcao == 3:
    print(f'\nVocê Escolheu pagar em duas vezes no cartão! \nValor do produto: {p} \nValor das prestações a serem pagas: {p/2}')
elif opcao == 4:
    d = int(input('\nVocê Escolheu pagar no cartão!\nQuer pagar em quantas vezes?: '))
    print(f'\nValor do produto: {p} Reais\nValor a ser pago em {d} prestações: {(p + (p * 0.2)) / d} Reais')
    print(f'Valor total das prestações: {p + (p * 0.2)} Reais')
else:
    print('\nOpção invalida!!!')

print('\nObrigado pela compra!!!')              