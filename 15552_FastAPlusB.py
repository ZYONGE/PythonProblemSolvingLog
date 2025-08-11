# Use sys.stdin.readline() for faster input then built-in input().
# Avoids the overhead of Python's default input()
import sys
#.rstrip() removes trailing whitespace characters, including the newline '\n'
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
i = 1

while i<n+1:
    a, b = map(int,input().split())
    print(a+b)
    i+=1
