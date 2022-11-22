#-6: Faça um Programa que leia cinco números e mostre o maior e o menor deles.
x=-1
numeros =[]
while x>0:
    num = int(input("informe um número: "))
    numeros.append(num)
    x-=1
print(min(numeros))
print(max(numeros))