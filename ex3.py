#Conte os espaços e vogais: Dado uma string com uma frase informada pelo usuário
#(incluindo espaços em branco), conte:
#1. quantos espaços em branco existem na frase.
#2. quantas vezes aparecem as vogais a, e, i, o, u.

contador = 0

frase = input('Digite sua frase: ')

for letra in frase:
    
    if 'a'==letra:
        contador += 1
    elif ' '==letra:
        contador += 1
    elif 'e'==letra:
        contador += 1
    elif 'i'==letra:
        contador += 1
    elif 'o'==letra:
        contador += 1
    elif 'u'==letra:
        contador += 1
    else:
        continue

print(f'O numero total é de: {contador}')