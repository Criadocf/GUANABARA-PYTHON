y = input('DIGITE QUALQUER COISA: ')
print('O tipo primitivo é', type(y))
print(f'Só tem espaços? {y.isspace()}')
print(f'É alfabético? {y.isalpha()}')
print(f'É numérico? {y.isnumeric()}')
print(f'É alfanumérico? {y.isalnum()}')
print(f'É maiúscula? {y.isupper()}')
print(f'É minúsculo? {y.islower()}')