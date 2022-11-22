# -1: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("informe um numero de 0 a 10: "))

while nota>10 or nota<0: #Parametro para delimitar entre 10 e 0.
	nota=float(input("número inválido! Por favor, informe um numero de 0 a 10: "))

print(f'A nota escolhida é: {nota}')