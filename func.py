'''def outer(arg):
    print('outer is started')
    print(arg)
    def inner():
        print('inner func is started')
        arg()
        print('inner func is ended')
    print('outer is ended')
    return inner
@outer
def wish():
    print('wish func is started')
    print('wish func id ended')
wish()'''


'''def outer(arg):
    def inner():
        print('sailu has taken the call')
        
        arg()
        print('sailu has ended the call')
    return inner

@outer
def indu():
    print('indu has started speaking')
    print('indu has ended speaking')
indu()

@outer
def arvind():
    print('arvind started speaking')
    print('arvind ended speaking')
arvind()'''

#happy number
'''n=int(input('enter number'))
summ=0
while(True):
    while(n>0):
        rem=n%10
        n=n//10
        summ+=rem*rem
    n=summ
    if summ==1:
        print('happy number')
        break
    else:
        print('not a happy number')
    summ=0'''


#pronic number

'''n=int(input('enter number'))
flag=0
for i in range(1,n+1):
    if(i*(i+1)==n):
        flag+=1
        break
if flag==1:
    print(n,"is pronic number")
else:
    print(n,'not a pronic numner")'''

#sunny number

'''n=int(input('enter number'))

n1=n+1
flag=0
for i in range(1,n1):
    if i*i==n1:
        flag+=1
        break
if flag==1:
    print(n,"is a sunny number")
else:
    print(n,"is not a sunny number")'''


#fascnating number

'''n=int(input('enter number'))
l=len(str(n))
if l!=3:
    print('fanscinating number check cant be done')
else:
    n1=n
    n2=n*2
    n3=n*3
    res=str(n1)+str(n2)+str(n3)
    print(res)
    flag=0
    for num in res:
        if len(res)!=9 or res.count(num)>1 or res.count(num)==0:
            flag+=1
            break
if flag==1:
    print(n,"is not a fanscinating number")
else:
    print(n,"is a fanscinating number")'''

#spy number

'''n=int(input('enter number'))
dummy=n
summ=0
prod=1
while dummy>0:
    rem=dummy%10
    summ=summ+rem
    prod=prod*rem
    dummy=dummy//10
if summ==prod:
    print(n,"is spy number")
else:
    print(n,"is not spy number")

'''

#automorphic number

'''n=int(input('enter number'))
dummy=n
sq=dummy**2
t=10
flag=0
while n>0:
    rem=sq%10
    if rem==dummy:
        flag+=1
        break
    dummy=dummy//10
    t=t*10
if flag==1:
    print('square number is',sq)
    print(dummy,'is automorphic number')
else:
    print(dummy,'is not automorphic number')'''


#ugly number
'''n=int(input('enter number'))
dummy=n
if dummy>0:
    for i in[2,3,5]:
        while dummy%i==0:
            dummy/=i
if dummy==1:
    print(n,'is a ugly number')
#input=2 or 5 or 9 or 12 or 15'''


'''def is_ugly(num):
    if num==0:
        return False
    for i in[2,3,5]:
        while num%i==0:
            num/=i
    return num==1
print(is_ugly(15))'''

'''#magic number
n=int(input('enter number'))
dummy=n
while dummy>=10:
    summ=0
    while dummy>0:
        rem=dummy%10
        summ=summ+rem
        dummy=dummy//10
    dummy=summ
if summ==1:
    print(n,'is a Magic number')
else:
    print(n,'is not a Magic number')

#input=1234 or 532 or 64 ect...
#finding the sum of all individual digits untill u get the sum as a single number'''


#Evil number

'''n=int(input('enter number'))
dummy=n
l=[]
while dummy!=0:
    rem=dummy%2
    l.append(rem) #list with all remainders
    dummy=dummy//2

l.reverse()
print('Binary equivalent of', n ,"is:")
for i in l:
    print(i,end=" ")
c=l.count(1) #c is having count of 1's in binary equivalent
if c%2==0:
    print("\n",n,"is evil number")
else:
    print("\n",n,"is not evil number")'''

#Tech Number

n=int(input('enter number'))
dummy=n
l=int(len(str(n)))
if l%2==0:
    p=1
    for i in range(int(l/2)):
        p=p*10
    rem=dummy%p
    dummy=int(dummy/p)
    sum=rem+dummy
    res=sum*sum
if res==n:
    print(n,"is a tech number")
else:
    print(n,"is not a tech number")

#input=2025

    
    
    
    
          















