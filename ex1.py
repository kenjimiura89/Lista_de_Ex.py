# 1- Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings possuem o mesmo
# comprimento e são iguais ou diferentes no conteúdo.
# Compare duas strings
# String 1: Brasil Hexa 2022
# String 2: Brasil! Hexa 2022!

frase1 = 'Brasil Hexa 2022'
len_frase1 = len(frase1)

frase2 = 'Brasil! Hexa 2022!'
len_frase2 = len(frase2)

if len_frase1 == len_frase2:
    print('possuem o mesmo comprimento!')
else:
    print('Não possuem o mesmo comprimento!')