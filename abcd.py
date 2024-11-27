'''n=int(input('enter number'))
n1=int(input())
row=n
while row<=n1:
    col=n
    while col<=n1:
        
        print('*',end=' ')
        
        col+=1
    row+=1

print()'''

'''n=int(input('enter number'))
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*', end=' ')
    print()'''

'''n=int(input('enter number'))
row=0
while row<n:
    col=0
    while col<n:
        print('*',end=' ')
        col+=1
    row+=1
    print()'''

#using break
'''n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==n:
            break
        print('*',end=' ')
    print()'''

#for
'''n=int(input('enter number'))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


#while
'''n=int(input())
row=0
while row<n:
    col=0
    while col<n:
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        col+=1
    row+=1
    print()'''

'''n=int(input('enter number'))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
n=int(input('enter number'))
row=0
while row<n+1:
    col=0
    while col<n+1:
        if row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        col+=1
    row+=1
    print()'''

'''n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col or row+col==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row<=col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

         
'''n=int(input())
for row in range(0,n+1):
    for col in range(1,n-row):
        print('*',end=' ')
        
    print()'''


# right triangle star pattern
'''n=int(input())
for row in range(0,n+1):
    for col in range(1, n - row):
        print(" ", end="")
    for k in range(0, row + 1):
        print("*", end="")
    print()'''


# right triangle star pattern
'''size = 5
for i in range(0,size+1):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(0, i + 1):
        print("*", end="")
    print()'''


'''n=int(input())
sp=0
st=n
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end='  ')
    for st in range(1,st+1):
        print('*',end='  ')
    print()
    sp+=1
    st-=1'''

'''n=int(input())
sp=n-1
st=1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end='  ')
    for st in range(1,st+1):
        print('*',end='  ')
    print()
    sp-=1
    st+=1'''

'''n=int(input())
num=1
for row in range(1,n+1):
    for num in range(1,num+1):
        print(num,end='  ')
    print()
    num+=1'''
'''n=int(input())
st=n
for row in range(1,st+1):
    for st in range(1,st+1):
        print('*',end='  ')
    print()
    st-=1'''

'''n=int(input('enter number'))
sp=n//2
st=1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end='  ')
    for st in range(1,st+1):
        print('*',end='  ')
    print()
    if row<=n//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2'''

'''n=int(input('enter number:'))
sp=n//2
st=1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end='  ')
    for st in range(1,st+1):
        print('*',end='  ')
    print()
    if row<n//2+1:
        sp-=1
        st+=1
    else:
        sp+=1
        st-=1'''
'''n=int(input('enter number:'))
sp=0
st=n
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print('*',end=' ')
    print()
    if row<n//2+1:
        sp+=1
        st-=2
    else:
        sp-=1
        st+=2'''
'''n=int(input('enter number:'))
sp=0
st=1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print('*',end=' ')
    if row<n//2+1:
        st+=1
    else:
        sp+=1
        st-=1'''

#number type pattern---->
'''n=int(input())
st=n
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        if row+col<=n+1:
            print(dummy,end='  ')
            dummy+=1
    print()
    st+=n'''

'''n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end='  ')
        dummy+=n
    print()'''

'''n=int(input())
sp=0
st=1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print('  ',end=' ')
    for st in range(1,st+1):
        print('*',end='  ')
    print()
    if row<=n//2:
        sp+=1
    else:
        sp-=1'''
'''n=int(input())
sp=n//2
st=1
for row in range(1,n+1):
    for sp in range(1,sp+1):
        print(' ',end=' ')
    for st in range(1,st+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        sp-=1
    else:
        sp+=1'''


'''n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end='  ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()'''

'''n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(dummy,end='  ')
        dummy+=row
    print()'''

'''n=int(input())
st=n
dummy=1
for row in range(1,n+1):
    for st in range(1,st+1):
        print(dummy,end='  ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    st-=1'''

        
'''n=int(input())
st=n
for num in range(1,n+1):
    for i in range(1,n+1):
        print(num,end='  ')
    print()
    st+=1'''

'''n=int(input())
st=1
num=1
for row in range(1,n+1):
    for st in range(1,st+1):
        print(num,end=' ')
        
    print()
    st+=1
    num+=1'''

'''n=int(input())
st=1
ascii=65
for row in range(1,n+1):
    for st in range(1,st+1):
        alp=chr(ascii)
        print(alp,end=' ')
    print()
    st+=1
    ascii+=1'''


'''n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end='  ')
        dummy+=row
    print()'''


'''n=int(input())
stars=n
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(64+dummy),end='  ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    stars-=1'''


'''n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    spaces-=1
    stars+=2'''

'''n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
    print()
    dummy+=1'''

'''n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()'''

''''n=int(input())
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(dummy,end=' ')
        dummy+=1
    print()'''

'''n=int(input())
stars=1
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(dummy,end=' ')
    print()
    dummy+=1
    stars+=1'''


#alphabet patterns------>

'''n=int(input())
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()'''

'''n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()'''

'''n=int(input())
dummy=1
for row in range(1,n+1):
    for col in range(1,n+1):
        print(chr(64+dummy),end=' ')
    print()
    dummy+=1'''

'''n=int(input())
stars=1
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
    print()
    dummy+=1
    stars+=1'''

'''n=int(input())
stars=1
for row in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars+=1'''
        
'''n=int(input())
stars=1
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars+=1'''


'''n=int(input())
spaces=n-1
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    stars+=1
    spaces-=1'''

'''n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end=' ')
        dummy+=row
    print()'''

'''n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy+=2
    print()'''

'''n=int(input())
stars=n
dummy=1
for row in range(1,n+1):
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if row%2==1:
            dummy+=1
        else:
            dummy-=1
    print()
    stars-=1'''

'''n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        dummy+=1
    print()
    spaces-=1
    stars+=2'''
        

'''n=int(input())
spaces=n-1
stars=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if st<=stars//2:
            dummy+=1
        else:
            dummy-=1
    print()
    spaces-=1
    stars+=2'''

'''n=int(input())
spaces=n//2
stars=1
for row in range(1,n+1):
    dummy=1
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
        if st<=stars//2:
            dummy+=1
        else:
            dummy-=1
    print()
    if row<=n//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2'''

'''n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(64+dummy),end=' ')
        dummy+=n
    print()'''

'''n=int(input())
spaces=0
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(dummy,end=' ')
    print()
    if row<=n//2:
        dummy+=2
        spaces+=1
    elif row==n//2+1:
        dummy-=1
        spaces-=1
    else:
        dummy-=2
        spaces-=1'''

'''n=int(input())
spaces=0
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
    print()
    if row<=n//2:
        dummy+=2
        spaces+=1
    elif row==n//2+1:
        dummy-=1
        spaces-=1
    else:
        dummy-=2
        spaces-=1'''
    
n=int(input())
spaces=n//2
stars=1
dummy=1
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(64+dummy),end=' ')
    print()
    if row<=n//2:
        dummy+=2
        spaces-=1
    elif row==n//2+1:
        dummy+=1
        spaces+=1
    else:
        dummy-=2
        spaces+=1
        

    
        















