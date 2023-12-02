import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
2 3 3
2 1
10 30 20
1 2
2 1
2 3
2 1 0
1000000000 1
1000000000
10 10 10
47718 21994 74148 76721 98917 73766 29598 59035 69293 29127
7017 46004 16086 62644 74928 57404 32168 45794 19493 71590
1 3
2 6
4 5
5 4
5 5
5 6
5 7
5 8
5 10
7 3
"""

def solve(test):
  N,M,L=map(int, input().split())
  a=list(map(int, input().split()))
  b=list(map(int, input().split()))
  c=[list(map(int, input().split())) for _ in range(L)]
  d=sorted([(b[i],i) for i in range(M)], reverse=True)
  s=[set() for _ in range(N)]
  for i in range(L):
    s[c[i][0]-1].add(c[i][1]-1)
  ans=0
  for i in range(N):
    for j in range(M):
      if d[j][1] not in s[i]:
        ans=max(ans,a[i]+d[j][0])
        break
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)