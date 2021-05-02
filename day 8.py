
#1
def isprime(n):
    c=0
    for i in range(2,n+1):
        if n%i==0:
            c+=1
    if c==1:
        print('prime')
    else:
        print('not prime')

n=int(input())
isprime(n)

#2
def fact(n):
    c=1
    for i in range(n,0,-1):
        c=c*i
    print('factorial is : ',c)

n=int(input())
fact(n)
