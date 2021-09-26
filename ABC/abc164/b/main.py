import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
a,b,c,d = LI()
win = 0
while (a > 0 and c > 0):
    c -= b
    if c <= 0:
        win = 1
        break
    a -= d
    if a <= 0:
        win = 2
        break

if win == 1:
    print('Yes')
else:
    print('No')