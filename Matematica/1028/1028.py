import math
n = int(input())
for i in range(n):
    fig = list(map(int, (input().split())))
    fig1 = fig[0]
    fig2 = fig[1]
    print(math.gcd(fig1, fig2))
