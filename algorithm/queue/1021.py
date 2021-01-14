import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

nums = map(int, sys.stdin.readline().split())

q = deque(range(1, n+1))

total = 0

