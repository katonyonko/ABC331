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
7 8
abcbacb
2 1 5
2 4 7
2 2 2
1 5 c
2 1 5
2 4 7
1 4 c
2 3 6
"""

class SegTree:
    X_unit = 0
    X_f = lambda self, x, y: x + y
 
    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)
 
    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
 
    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
 
    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def get_val(self,idx):
        return self.X[idx+self.N]

def solve(test):
  N,Q=map(int, input().split())
  S=input()
  T = tuple(map(lambda x: ord(x)-96, S))
  mod = 10**9+7
  st1=SegTree(N)
  st2=SegTree(N)

  H = [None] * N
  for i in range(N):
      H[i] = T[i]*pow(100,i,mod) % mod

  H_rev = [None] * N
  for i in range(N):
      H_rev[i] = T[N-i-1]*pow(100,i,mod) % mod
  st1.build(H)
  st2.build(H_rev)
  # print(st1.fold(0,3))
  def if_palindrome(l, r):
      h = st1.fold(l-1,r)*pow(100,(l-1)*(mod-2),mod) % mod
      h_r = st2.fold(N-r,N-l+1)*pow(100,(N-r)*(mod-2),mod) % mod
      # print(l,r,h,h_r)
      return 'Yes' if h == h_r else 'No'


  for i in range(Q):
    d,l,r=input().split()
    if d=='1':
      l=int(l)
      st1.set_val(l-1,(ord(r)-96)*pow(100,l-1,mod) % mod)
      st2.set_val(N-l,(ord(r)-96)*pow(100,N-l,mod) % mod)
    else:
      l,r=int(l),int(r)
      print(if_palindrome(l,r))
    # print([st1.get_val(i) for i in range(N)])
    # print([st2.get_val(i) for i in range(N)])

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