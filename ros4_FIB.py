#!/bin/python

n = raw_input("n?") #g eneration number
k = raw_input("k?") # pairs per mate pair

#convert to ints
n = int(n)
k = int(k)

F = [1,1] #initialize Fib as list

for i in range(2,n):
	next = F[i-1] + F[i-2]*k
	F.append(next)

print F[n-1]

