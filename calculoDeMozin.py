n = int(input("Digite até que número nossa conta vai :"))

soma = 0
for i in range (1, n+1):
    pot = 1
    for j in range (0, i):
        pot = pot * i
    soma = soma + pot      
print(soma)