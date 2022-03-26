n = int(input())
c = {1:0, 2:1}

def dp(n):
    if n in c:
        return c[n]

    cnt = 1 + min(dp(n//3) + n%3, dp(n//2) + n%2)
    c[n] = cnt
    return cnt

print(dp(n))
