#1
l1=[1,2,3,4]
l2=['a','b','c','d']
d=dict(zip(l1,l2))
print(d)


#2

n=input()
l1=[]
l2=[]
for i in n:
    if 97<=ord(i)<=122 or 65<=ord(i)<=90:
        l1.append(i)
    elif i in """0123456789""":
        l2.append(i)
print("Letters : ",len(l1))
print("Digits : ",len(l2))


#3

n=input()
n=n.split()
print(n)
f=0
count=len(n[0])
for i in range(1,len(n)):
    if len(n[i])>=count:
        count=len(n[i])
        print('length of longest word is : ',n[i],':',len(n[i]));f=1
if f==0:
    print('length of longest word is : ',n[0],':',len(n[0]))
    

#4

n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end='')
    print()
    

#5 RUSSIAN PRIME 

def isprime(n):
    c=0;f=0
    for i in range(2,n+1):
        if n%i==0:
            c=c+1
    if c==1 and n!=0:
        print('prime',n) 
        n=n//10
        return isprime(n)
    else:
        return True
    
n=int(input())
s=isprime(n)
if s==True:
    print("ITS A RUSSIAN PRIME",n )
else:
    print("NOT A RUSIAN PRIME")
    


