#-5: Faça um programa que calcule e mostre a média aritmética de N notas.
# N notas = o usuário pode selecionar a quantidade de notas
qntd = 0
N = []
resposta = 's'
while resposta in 's':
    valor = float(input('Digite um valor: '))
    qntd +=1
    N.append(valor)
    resposta = str(input('Adicionar mais valores? [s/n]: '))
soma = sum(N)
media = soma / qntd
print(f"Você digitou: {qntd} números e a média deles são de: {media} ")
