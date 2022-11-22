# -4: Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
N = []
resposta = 's'
while resposta in 's':
    num = int(input('Digite um valor: '))
    N.append(num)
    resposta = str(input('Adicionar mais valores? [s/n]: '))
(min(N))
(max(N))
(sum(N))
print(f'o menor valor é: {min(N)}, o maior valor é: {max(N)} e a soma dos valores são: {sum(N)}')