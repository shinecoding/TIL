#이항계수를 구하라 = 조합(Combination)을 구하라
import math

n, k = map(int, input().split())

print(math.factorial(n) // (math.factorial(n-k) * math.factorial(k)))