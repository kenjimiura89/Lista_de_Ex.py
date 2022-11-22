#Valide e corrija o número de telefone. Faça um programa que leia um número de
#telefone, e corrija o número no caso deste conter somente 7 dígitos, adicionando o '9' na
#frente. O usuário pode informar o número com ou sem o traço separador.

#Valida e corrige número de telefone
#Telefone: 461-0133
#O telefone possui 9 dígitos. Vou acrescentar o dígito nove na frente.
#Telefone corrigido sem formatação: 34610133
#Telefone corrigido com formatação: 93461-0133

numero = int(input('Isira o número de Telefone: ')) #numero da pessoa.
adicione = '9' #valor a ser adicionado dentro da condição

if len(str(numero)) < 8: #se caso o numero for menor do que 7, adicionar (COMOOOOO??????????)
    corrigido = adicione + str(numero) #Como 'len' somente lê em str, logo coloco o str em frente para adicionar o 0 na frente.
    print(corrigido) #resultado

#Lembrar de verificar com a Isa se entendi o exercício correto ><