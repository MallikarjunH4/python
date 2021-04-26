n,m=map(int,input().split(' '))
for i in range(n,m):
    if i%5==0 and i%7==0:
        print(i,end='  ')
#2
n=input()
m=int(input())
s=0
for i in range(1,m+1):
    a=n*i
    s=s+int(a)
print(int(s)
#3
c=2
sum=0
while c!=0:
    n=int(input())
    if n==-1:
        c=0
    sum=sum+int(n)
print(int(sum))
#4
n=int(input())
f=1
for i in range(n,0,-1):
    f=f*i
print(f)

