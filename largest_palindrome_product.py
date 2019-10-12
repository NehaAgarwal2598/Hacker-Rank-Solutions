# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

#!/bin/python3

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p = 0
    for a in range(n-1, 10000, -1):
        if str(a)==str(a)[::-1]:
            for b in range(100, 1000):
                if a%b==0 and a//b<999:
                    p = a
                    break
            if p != 0:
                print(p)
                break
