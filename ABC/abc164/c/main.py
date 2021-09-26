import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return tuple(sys.stdin.readline().rstrip().split())
N = I()
A = [LS() for _ in range(N)]
l = set(A)
print(len(l))