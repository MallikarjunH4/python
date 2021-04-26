# age 
n=int(input())
print('current age of the person is:',2021-n-1)

#calculator
n,m=map(int,input().split())
print('ADD is:'+str(m+n),'SUB is:'+str(n-m),'MULTI is :'+str(n*m),'FLOORDIV is :'+str(n//m),'DIV is :'+str(n/m),'REM is:'+str(n%m),'POWER is :'+str(n**m),sep='\n')

#count
n=input()
print(n.count('y'))

#even index
n=input()
for i in n[0::2]:
    print(i,end=' ')