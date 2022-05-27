salario = float(input('DIGITE SEU SALÁRIO ATUAL: R$'))
porcentagem_aumento = float(input('DIGITE QUAL A PORCENTAGEM DO SEU AUMENTO: %'))
aumento = porcentagem_aumento/100

print(f'Seu salário de R${salario} com o aumento de R${aumento}, passa a ser de {salario+(salario*aumento):.2f}')