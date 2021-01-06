import math

n, k = map(int, input().split())

nk = math.factorial(n) // (math.factorial(k)* math.factorial(n-k))
print(nk%10007)