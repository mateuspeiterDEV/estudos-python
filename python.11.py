d = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
d1 = d * 60
km1 = km * 0.15
soma = d1 + km1
print('O total a pagar é de R${:.2f}'.format(soma))
int(input('Pressione ENTER para continuar'))
