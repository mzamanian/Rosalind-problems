#!/bin/python

n = raw_input("n?") # generation number
m = raw_input("m?") # months alive

#convert to ints
n = int(n)
m = int(m)

F = [1,1] # Initialize Fib as list
N = [1,0] # New rabbits
NM = [0,1] # New mature rabbits
M = [0,1] # Total mature rabbits
D = [0,0] # New dead rabbits


for i in range(2,n):
	NM.append(N[i-1]) #define NM (new mature) as N (new) from previous iteration 
	M.append(sum(NM[-m+1:])) #define M (total mature) as sum of last m-1 iterations of NM (newly mature)
	N.append(M[i-1]) #define N (new rabbits) as M (total mature) previous previous iteration
	if i < m:
		D.append(0)
	else:
		D.append(NM[i-m+1]) #define D (newly dead) as NM from m iterations ago
	F.append(F[i-1] + N[i] - D[i])  #new total number of rabbits = previous + new - dead
print F[n-1]


#OR
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in xrange(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)
