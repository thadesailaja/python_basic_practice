#for loop inside another for loop(OL)-->
'''for i in range(1,6):
    for j in range(1,6):
        print(i,j)'''

#breaking inner loop with inner loop value

'''for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if j==3:
            break

for i in range(1,6):
    for j in range(1,6):
        if j==3:
            break
        print(i,j)'''
        
#breaking inner loop with outer loop value

'''for i in range(1,6):
    for j in range(1,6):
        if i==3:
            break
        print(i,j)'''

#breaking outer loop with outer loop value
'''for i in range(1,6):
    if i==3:
        break#continue
    for j in range(1,6):
        print(i,j)

for i in range(1,6):
    if i==3:
        for j in range(1,6):
            print(i,j)
        break#(31,32,33,34,35)'''

#breaking outer loop with inner loop value
'''for i in range(1,6):
    if j==3:
        break
    for j in range(1,6):
        print(i,j)
#NameError: name 'j' is not defined

for i in range(1,6):
    for j in range(1,6):
        print(i,j)
    if j==5:
            break'''

#While loop inside another while loop--->

'''i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    i+=1'''

#breaking inner loop with inner loop value
'''i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if j==4:
            break
        j+=1
    i+=1'''

#breaking inner loop with outer loop value
'''i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        j+=1
    i+=1'''

#breaking outer loop with outer loop value
'''i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if i==3:
        break
    i+=1'''

#breaking outer loop with inner loop value
'''i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break
    i+=1'''

#for loop inside another while loop--->

'''for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        i+=1'''

#breaking inner loop with inner loop value
'''for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        if j==3:
            break
        j+=1'''

#breaking inner loop with outer loop value
'''for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        if i==3:
            break
        j+=1'''

#breaking outer loop with outer loop value
'''for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        j+=1
    if i==3:
        break'''
#breaking outer loop with inner loop value
'''for i in range(1,6):
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break'''

'''i=1
while i<6:
    for j in range(1,6):
        print(i,j)
        if j==3:
            break
    i+=1'''

'''i=1
while i<6:
    for j in range(1,6):
        print(i,j)
        if i==3:
            break
    i+=1'''

'''i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    if i==3:
        break
    i+=1'''
    
'''i=1
while i<6:
    for j in range(1,6):
         if j==3:
            break
         print(i,j)
   
    i+=1'''


#WAP to print all prime numbers in a given range
#for inside for
'''LL=int(input())
UL=int(input())
for i in range(LL,UL+1):
    if i>1:
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)'''

#while inside while
'''LL=int(input())
UL=int(input())
num=LL
while num<=UL:
    if num>1:
        i=2
        while i<=num//2:
            if num%i==0:
                break
            i+=1

        else:
            print(num)
    num+=1'''

#while inside for

'''LL=int(input())
UL=int(input())
for num in range(LL,UL+1):
    if num>1:
        i=2
        while i<num//2+1:
            if num%i==0:
                break
            i+=1
        else:
            print(num)'''
#for inside while
'''LL=int(input())
UL=int(input())
num=LL
while num<UL+1:
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            print(num)
    num+=1'''

#WAP to print perfect numbers in a given range
#for inside for
'''LL=int(input())
UL=int(input())
for num in range(LL,UL+1):
    sum=0
    for i in range(1,num//2+1):
        if num%i==0:
            sum=sum+i
            if sum==num:
               print(num)'''
#while inside while
'''LL=int(input())
UL=int(input())
num=LL
while num<UL+1:
    sum=0
    i=1
    while i<num//2+1:
        if num%i==0:
            sum=sum+i
        i+=1
        if sum==num:
            print(num)
    num+=1'''

#for inside while
'''LL=int(input())
UL=int(input())
num=LL
while num<UL+1:
    summ=0
    for i in range(1,num//2+1):
        if num%i==0:
            summ=summ+i
            if summ==num:
                print(num)
    num+=1'''
#while inside for
LL=int(input('enter LL number:'))
UL=int(input('enter UL number:'))
for a in range(LL,UL+1):
    sum=0
    b=1
    while b<a//2+1:
        if a%b==0:
            sum=sum+b
            if sum==a:
               print(a)
        b+=1













