n = float(input())

n100 = n//100

n -= n100*100

n50 = n//50

n -= n50*50

n20 = n//20

n -= n20*20

n10 = n//10

n -= n10*0.10

n5 = n//5

n -= n5*5

n2 = n//2
n -= n2*2

#moedas
n1 = n//1
n -= n1*1

n050 = n//0.5

n -= n050*0.5

n025 = n//0.25
n -= n025*0.25

n010 = n//0.10
n -= n010*0.10

n05 = n//0.05
n -= n05*0.05

n01 = n//0.01
n -= n01*0.01


print("NOTAS:")
print('{:.0f} nota(s) de R$ 100.00'.format(n100))
print('{:.0f} nota(s) de R$ 50.00'.format(n50))
print('{:.0f} nota(s) de R$ 20.00'.format(n20))
print('{:.0f} nota(s) de R$ 10.00'.format(n10))
print('{:.0f} nota(s) de R$ 5.00'.format(n5))
print('{:.0f} nota(s) de R$ 2.00'.format(n2))
print("MOEDAS:")
print('{:.0f} moeda(s) de R$ 1.00'.format(n1))
print('{:.0f} moeda(s) de R$ 0.50'.format(n050))
print('{:.0f} moeda(s) de R$ 0.25'.format(n025))
print('{:.0f} moeda(s) de R$ 0.10'.format(n010))
print('{:.0f} moeda(s) de R$ 0.05'.format(n05))
print('{:.0f} moeda(s) de R$ 0.01'.format(n01))
