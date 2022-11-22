#-6: Faça um Programa que leia cinco números e mostre o maior e o menor deles.

A = int(input("informe um número para A: "))
B = int(input("informe um número para B: "))
C = int(input("informe um número para C: "))
D = int(input("informe um número para D: "))
E = int(input("informe um número para E: "))

conjunto = [A, B, C, D, E]
print(conjunto)

if A<B and A<C and A<D and A<E:
    menor = A
if B<A and B<C and B<D and B<E:
    menor = B
if C<A and C<B and C<D and C<E:
    menor = C
if D<A and D<B and D<C and D<E:
    menor = D
if E<A and E<B and E<C and E<D:
    menor = E
if A>B and A>C and A>D and A>E:
    maior = A
if B>A and B>C and B>D and B>E:
    maior = B
if C>A and C>B and C>D and C>E:
    maior = C
if D>A and D>B and D>C and D>E:
    maior = D
if E>A and E>B and E>C and E>D:
    maior = E

print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')