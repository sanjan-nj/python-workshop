''' code: 1
user_id=input('enter user_id : ')
id='sanjan'
pwd='sanjan@1'
if user_id!=id:
    print("invalid password") 
else:
    password=input("enter a password:")
    if password==pwd:
        print("login successful")
    else:
        print("invalid password")'''
#code:2
'''marks=int(input("Enter your Marks : "))
if 0<=marks<=100:
    if marks<=80:
        print("Your grade is A+")
    elif 60<=marks<80:
        print("Your grade is A")  
    elif 50<=marks<60:
        print("Your grade is B") 
    elif 35<=marks<50:
        print("your grade is C")
    else:
        print('Your fail')'''
#code : 3
# even number between 10 and 20
'''
i=10
while i<=20:
    if i % 2 == 0:
        print(i)
    i+=1
'''
#  code 4
# odd number between 30 and 12
'''
i=30
while i>=12:
    if i % 2 == 1:
        print(i)
    i-=1
'''   
# code 5
# a='CSISESYSS' output='ssss'
'''
a='CSISESYSS'
i=0
b=''
while i<=len(a):
    if i % 2 == 1:
        b = b + a[i]
    i+=1
print(b)            
'''
# code 6
# a=[19,2,13,4,5,11,-1,-17] output=48
'''
a=[19,2,13,4,5,11,-1,-17]
i=0
b=0
while i<len(a):
    if a[i] <=0:
        if a[i] % 2 == 1:
            b = b + a[i]
    i+=1
print(b)  
'''  
# program 7
'''
a='Prof123@gmail.com' 
b='' 
c=''
d=''
i=0
while i<len(a):
    if 'a'<=a[i]<='z' or 'A'<=a[i]<='Z':
        b=b+a[i] 
    elif '0'<=a[i]<='9':
        c=c+a[i]  
    else:
        d=d+a[i]  
    i+=1
print(f"b={b},c={c},d={d}")
'''
# program 8
'''
a='ABCD'
i=0
b=''
while i<len(a):
    if 'A'<=a[i]<='Z':
        b=b+chr(ord(a[i])+32)
    i+=1
print(b) 
'''
# 10/9/25 program 1 (for loop)
'''
a='12345'   
for i in a:
    print("12345")
'''
# program 2
''' 
for i in range(6,13):
    if i % 2 == 0:
        print(i)
'''
'''
b='teacher'
c=0
for i in range(1,8,2):
    c=c+i
print(c) 
'''
b='swampodaya Exskilence'
i=0
c=0
while len(b)>i:
    if 'aeiou' in b[i]:
        c=c+1
    i=i+1
print(c)              


           

    
        
