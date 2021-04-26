n=list(map(int,input().split(' ')))
c=0
c1=0
for i in n:
    if i%2==0:
        c=c+1
    else:
        c1=c1+1
print('even',c)
print('odd',c1)
#2
n=list(map(int,input().split(' ')))
max=n[len(n)-1]
min=n[0]
for i in range(len(n)):
    if n[i] < min: 
        min = n[i] 
    else: 
        if n[i] > max: 
            max = n[i]
print('max',max)
print('min',min)
#3
n=list(map(int,input().split(' ')))
l=[]
l=n[::-1]
if n==l:
    print('palindrome')
else:
    print('not palindrome')