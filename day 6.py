# day 6
# 1
n=list(input())
#s=""aeiouAEIOU""
for i in n:
    if i in s:
        print(n.index(i)+1)
        
#2
s='hello world happy birthday'
r= s.split()
r=r[::-1]
print(' '.join(r))

#3
s=[1,2,3,3,2,4]
l=[]
for i in s:
    if i not in l:
        l.append(i)
print(l)
