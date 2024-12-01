reais, centavos = map(int, input().split('.'))
centavos = centavos + reais * 100

print("NOTAS:")
print(f'{centavos//10000} nota(s) de R$ 100.00')
centavos = centavos%10000
print(f'{centavos//5000} nota(s) de R$ 50.00')
centavos = centavos%5000
print(f'{centavos//2000} nota(s) de R$ 20.00')
centavos = centavos%2000
print(f'{centavos//1000} nota(s) de R$ 10.00')
centavos = centavos%1000
print(f'{centavos//500} nota(s) de R$ 5.00')
centavos = centavos%500
print(f'{centavos//200} nota(s) de R$ 2.00')
centavos = centavos%200

print("MOEDAS:")
print(f'{centavos//100} moeda(s) de R$ 1.00')
centavos = centavos%100
print(f'{centavos//50} moeda(s) de R$ 0.50')
centavos = centavos%50
print(f'{centavos//25} moeda(s) de R$ 0.25')
centavos = centavos%25
print(f'{centavos//10} moeda(s) de R$ 0.10')
centavos = centavos%10
print(f'{centavos//5} moeda(s) de R$ 0.05')
centavos = centavos%5
print(f'{centavos//1} moeda(s) de R$ 0.01')
