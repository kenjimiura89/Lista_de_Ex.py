# -3: Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.
x=0
qntd=0
media = []
while x<10:
    A = float(input('Digite as suas notas: '))
    B = float(input('Digite as suas notas: '))
    C = float(input('Digite as suas notas: '))
    D = float(input('Digite as suas notas: '))
    soma = A + B + C + D
    media_aluno = soma / 4
    if media_aluno >= 7.0:
        qntd+=1
    media.append(media_aluno)
    x+=1
print(qntd)
