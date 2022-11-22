# -2: Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
# "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

positivo = 0 #valores a ser acrescentado de acordo com as respostas.
respostas = 's' #Indice que será contabilizado de acordo com a resposta, a cada 's' +1.

respostas = str(input('Telefonou para a vítima? [s/n] ? '))
if respostas == 's':
       positivo +=1 # A cada 's' será acrescentado +1.
else:
        positivo += 0

respostas = str(input('Esteve no local do crime? [s/n] ? '))
if respostas == 's':
        positivo +=1
else:
        positivo += 0

respostas = str(input('Mora perto da vítima? [s/n] ? '))
if respostas == 's':
        positivo +=1  
else:
        positivo += 0 

respostas = str(input('Devia para a vítima? [s/n] ? '))
if respostas == 's':
        positivo +=1                
else:
        positivo += 0

respostas = str(input('Já trabalhou com a vítima? [s/n] ? '))
if respostas == 's':
        positivo +=1 
else:
        positivo += 0
print(f'O número de respostas positivas é de {positivo}') # Irá mostrar a quantidade de 's' contabilizado.

# De acordo com o número de resposta, a pessoa será classificado.
if positivo == 2:
   print('Suspeita!')
elif positivo == 3:
   print('Cumplice!')
elif positivo == 4:
   print('Cumplice!')
elif positivo == 5:
   print('Assassino!')
else:
    print('Inocente!')