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
3 2
WWB
BBW
WBW
1 2 3 4
0 3 4 5
10 5
BBBWWWBBBW
WWWWWBBBWB
BBBWBBWBBB
BBBWWBWWWW
WWWWBWBWBW
WBBWBWBBBB
WWBBBWWBWB
WBWBWWBBBB
WBWBWBBWWW
WWWBWWBWWB
5 21 21 93
35 35 70 43
55 72 61 84
36 33 46 95
0 0 999999999 999999999
"""

def solve(test):
  N,Q=map(int, input().split())
  P=[input() for _ in range(N)]
  num=[]
  for i in range(N):
    for j in range(N):
      if P[i][j]=="B":
        tmp=1
      else:
        tmp=0
      if i>0: tmp+=num[(i-1)*N+j]
      if j>0: tmp+=num[i*N+j-1]
      if i>0 and j>0: tmp-=num[(i-1)*N+j-1]
      num.append(tmp)
  # for i in range(N):
  #   print(num[i*N:(i+1)*N])
  def calc(x,y):
    x1,y1=x%N,y%N
    x2,y2=x//N,y//N
    res=num[-1]*x2*y2+num[(N-1)*N+y1]*x2+num[x1*N+N-1]*y2+num[x1*N+y1]
    # print(num[-1]*x2*y2,num[(N-1)*N+y1]*x2,num[x1*N+N-1]*y2,num[x1*N+y1],x1,y1)
    return res
  # for i in range(N):
  #   for j in range(N):
  #     print(calc(i,j))
  # print(calc(5,21))
  for _ in range(Q):
    A,B,C,D=map(int, input().split())
    ans=calc(C,D)
    if A>0: ans-=calc(A-1,D)
    if B>0: ans-=calc(C,B-1)
    if A>0 and B>0: ans+=calc(A-1,B-1)
    print(ans)

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