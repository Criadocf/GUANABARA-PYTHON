preco_produto = float(input('DIGITE O VALOR DO PRODUTO: '))
juros = float(input('DIGITE A PORCENTAGEM DO DESCONTO %'))
desconto = juros/100

print(f'O preço do valor com desconto é de R${preco_produto-(preco_produto*desconto):.2f}')