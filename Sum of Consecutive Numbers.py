#The program takes a number N as input and output the sum of all numbers from 1 to N, including N.
N = int(input())
sum=0
for i in range(0,N+1):
    sum=sum+i
    i+=1
print(sum)
