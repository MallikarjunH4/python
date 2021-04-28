'''z=1
d={}
x=0
o=[]
def fun(d):
    o.append(d)
    print(o)
while z:
    print('1 : register \n2 : view enrolled \n0 : exit \n')
    z1=int(input())
    if z1==0:
        z=0
    if z1==2:
        fun(d)
    if z1==1:
        l1=[]
        print('enter your details to register : \n')
        r=input("enter user_id : ");r1=input("enter your name : \t");r2=input("enter your email : \t")
        user = {'user_id': r,'name': r1,'email': r2,
        'Allcourses' : {1:'Python', 2:'Java', 3:'Compiler Design', 4:'React JS', 5:'Finearts',6: 'Machine learning',7: 'Ruby', 8:'Database managemnet systems',9: 'Swift programming', 10:'Flutter framework',11: 'Oracle SQL',12: 'Artificial Intelligence'},
        'selectedcourses':[]}
        l1.append(r);l1.append(r1);l1.append(r2)
        f=1
        while f:
            choice=int(input("\nenter menu choice : \n1 : viewcourses & choose \n2 : see your courses \n3: edit your details\n0:main menu\n\n"))
            if choice == 0:
                f=0
            if choice == 1:
                print("\nselect any one of  the course shown below : \n")
                for key in user["Allcourses"]:
                    print(key, ' : ',user['Allcourses'][key])
                m=int(input("\npress the key valus of the course : "))
                user["selectedcourses"].append(user['Allcourses'][m])
                l1.append(user['Allcourses'][m])
                d[x+1]=l1

            elif choice == 2:
                c=1
                print("\nuser_id : ",user['user_id'],'\nname : ',user['name'],'\nemailid :',user['email'],'\nselected courses are : \n')
                for i in user['selectedcourses']:
                    print(c ,':' ,i,'\n\n')
                    c=c+1
            elif choice == 3:
                t=input("enter the new name : \t")
                user['name']=t;l1[1]=t
                t1=input("enter new mailid : \t")
                user['email']=t1;l1[2]=t1
''''
z=1
l1=[]
while z:
    i=1
    print('1 : register \n2 : view enrolled \n0 : exit \n')
    z1=int(input())
    if z1==0:
        z=0
    if z1==2:
        c=1
        print("\nuser_id : ",user['user_id'],'\nname : ',user['name'],'\nemailid :',user['email'],'\nselected courses are : \n')
        for i in user['selectedcourses']:
            print(c ,':' ,i,'\n\n')
            c=c+1        
        
    if z1==1:
        print('enter your details to register : \n')
        r=input("enter user_idonly numbers : ");r1=input("enter your name : \t");r2=input("enter your email : \t")
        user = {'user_id': r,'name': r1,'email': r2,
        'Allcourses' : {1:'Python', 2:'Java', 3:'Compiler Design', 4:'React JS', 5:'Finearts',6: 'Machine learning',7: 'Ruby', 8:'Database managemnet systems',9: 'Swift programming', 10:'Flutter framework',11: 'Oracle SQL',12: 'Artificial Intelligence'},
        'selectedcourses':[]}
        l1.append(r);l1.append(r1);l1.append(r2)
        f=1
        while f:
            choice=int(input("\nenter menu choice : \n1 : viewcourses & choose \n2 : see your courses \n3: edit your details\n0:main menu\n\n"))
            if choice == 0:
                f=0
            if choice == 1:
                print("\nselect any one of  the course shown below : \n")
                for key in user["Allcourses"]:
                    print(key, ' : ',user['Allcourses'][key])
                m=int(input("\npress the key valus of the course : "))
                user["selectedcourses"].append(user['Allcourses'][m])
                l1.append(user['Allcourses'][m])

            elif choice == 2:
                c=1
                print("\nuser_id : ",user['user_id'],'\nname : ',user['name'],'\nemailid :',user['email'],'\nselected courses are : \n')
                for i in user['selectedcourses']:
                    print(c ,':' ,i,'\n\n')
                    c=c+1
            elif choice == 3:
                t=input("enter the new name : \t")
                user['name']=t;l1[1]=t
                t1=input("enter new mailid : \t")
                user['email']=t1;l1[2]=t1

