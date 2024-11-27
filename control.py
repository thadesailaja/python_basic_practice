#FLOW CONTROL STATEMENTS----->

'''n=int(input())
if n>100:
    print('n is more than 100')

csk=int(input('enter runs of csk'))
mv=int(input('enter runs of mv'))
if csk>mv:
    print('if')
    print(f'csk{csk} is greater than mv{mv}')
else:
    print('else')
    print(f'mv{mv} is greater than csk{csk}')

s=input('enter string')
if s==s[::-1]:
    print('string is a palindrom')
else:
    print('string is not a palindrom')

s=input('enter string')
s1=input('enter string')
if sorted(s)==sorted(s1):
    print('given strings are anagrams')
else:
    print('given strings are not a anagrams')

n=int(input())
if n%2==0:
    print('even')
else:
    print('not a even')


n=int(input())
if n%2==0:
    print('even')
else:
    print('odd')'''


#leap year
'''
year=int(input('enter year'))
if(year%100!=0 and year%4==0) or (year%100==0 and year%400==0):
  print('year is a leap year')
else:
    print('is not a leap year')

num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print('num1 is the max num')
elif num2>num3:
    print('num2 is the max num')
else:
    print('num3 is the max num')


a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b and a>c and a>d:
    print('a is the max number')
elif b>c and b>d:
    print('b is the max number')
elif c>d:
    print('c is the max number')
else:
    print('d is the max number')


a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a==b==c==d:
    print('all numbers are equal numbers')

elif a>b and a>c and a>d:
    print('a is the max number')
    
elif b>c and b>d:
    print('b is the max number')
    
elif c>d:
    print('c is the max number')
    
else:
    print('d is the max number')



a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print('a is max')
    else:
        print('c is max')
else:
    if b>c:
        print('b is max')
    else:
        print('c is max')


a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print('a is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')
    else:
        if c>d:
            if c>e:
                print('c is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')
else:
    if b>c:
        if b>d:
            if b>e:
                print('b is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')
    else:
        if c>d:
            if c>e:
                print('c is max')
            else:
                print('e is max')
        else:
            if d>e:
                print('d is max')
            else:
                print('e is max')'''


#LOOPING STATEMENTS---->
#for loop-->

'''s=input('enter string')
c=0
for i in s:
    c+=1
print(c)

s=input('enter string')
s1=input('enter substring')
c=0
for i in s:
    if i==s1:
        c+=1
print(c)

s=input('enter string')
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c+=1
print(c)


s=input('enter string')
v='aeiouAEIOU'
c=0
for i in s:
    if i.isalpha() and i not in v:
        c+=1
print(c)


s=input('enter string')
v='aeiouAEIOU'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(vc)
print(cc)

s=int(input('enter string'))
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)

s=input()
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=k
print(sum)

s=input()
summ=0
for i in s:
    if i.isdigit():
        k=int(i)
        if int(i)%2==0:
            summ+=k
print(summ)

s=input('enter string')
es=0
cs=0
for i in s:
    if i.isdigit():
        k=int(i)
        if int(i)%2==0:
            es+=k
        else:
            cs+=k
print(abs(es-cs))

s=input('enter string')
c=0
for i in s:
    if not i.isalpha():
        c+=1
print(c)

l=input('enter list')
summ=0
for i in l:
    summ+=1
print(summ)


n=int(input())
summ=0
for i in range(1,n+1):
    summ+=i
print(summ)

n=int(input())
f=1
for i in range(1,n+1):
    f*=i
print(f)

n=int(input())
summ=0
for i in range(1,n//2+1):
    if n%i==0:
        summ+=i
if summ==n:
    print('n is a perfect number')
else:
    print('n is not a perfect number')

s=int(input())
e=int(input())
for i in range(s,e+1):
    if i%2==0:
        print(i)


            
s=int(input())
e=int(input())
for i in range(s,e+1):
    if i%2==0:
        print(i)

s=int(input())
e=int(input())
l=[]
for i in range(s,e+1):
    if i%2==0:
        l.append(i)
print(l[::2])

s=int(input())
e=int(input())
c=0
for i in range(s,e+1):
    if i%2==0:
        c+=1
        if c%2!=0:
            print(i)
s=int(input())
e=int(input())
c=0
for i in range(s,e+1):
    if i%2==0:
        c+=1
        if c%2==0:
            print(i)

s=int(input())
e=int(input())
l=[]
for i in range(s,e+1):
    if i%2==0:
        l.append(i)
print(l[1::2])


s=int(input())
e=int(input())
c=0
for i in range(s,e+1):
    if i%2==0:
        c+=1
        if c%3==0:
            print(i)

s=int(input())
e=int(input())
l=[]
for i in range(s,e+1):
    if i%2==0:
        l.append(i)
print(l[2::3])'''

#for loop with range and CDT--->

'''s='hello'
for ip in range(len(s)):
    print(ip,s[ip])


s='sailaja'
for ip in range(len(s)):
    print(ip,s[ip::])

n=input()
for i in range(len(n)):
    if n[i] in 'AEIOUaeiou':
        print(i,n[i])

n=input()
for i in range(len(n)):
    if n[i].isalpha and n[i] not in 'AEIOUaeiou':
        print(i,n[i])

n=input()
summ=0
for i in range(len(n)):
    if n[i].isdigit():
        summ+=int(n[i])
print(summ)

s='sailu2520'
summ=0
for i in s:
    if i.isdigit():
        summ+=int(i)
print(summ)

s=input()
summ=0
for i in range(len(s)):
    if s[i].isdigit():
        summ+=i
print(summ)

s=input()
sum=0
for i in range(len(s)):
    if s[i].isdigit():
        if int(s[i])%2==0 and i%2!=0:
          sum+=int(s[i])
print(sum)

s=input()
sum=0
for i in range(len(s)):
    if s[i].isdigit():
        if int(s[i])%2==0 and i%2==0:
            sum+=i
print(sum)

n=input()
summ=0
for i in range(len(n)):
    if n[i].isdigit():
        if int(n[i])%2!=0 and i%2==0:
            summ+=int(n[i])
print(summ)


s=input('enter string')
s1=input('enter sub string')
c=0
for i in range(len(s)):
    if s[i:i+len(s):]==s1:
        c+=1
print(c)

s=input()
s1=input()
summ=0
for i in range(len(s)):
    if s[i:i+len(s):]==s1:
        summ+=i
print(summ)

l=[10,21,6,7,9,15]
for ip in range(len(l)):
    if l[ip]%2==0:
        l[ip]='even'
    else:
        l[ip]='odd'
print(l)

l=[10,21,6,7,9,15]
l1=[]
for i in l:
    if i%2==0:
        l1.append('even')
    else:
        l1.append('odd')
print(l1)

a=4
while a>1:
    print('inside while block')
    a-=1

a=1
while a<10:
    print(a)
    a+=1

n=int(input())
summ=0
i=1
while i<=n:
    summ+=i
    i+=1

n=int(input())
f=1
i=1
while i<=n:
    f*=i
    i+=1

n=int(input())
sum=0
i=1
while i<=n//2:
    if n%i==0:
        sum+=i
        i+=1
if sum==n:
    print('perfect')
else:
    print('not a perfect')

s=input()
rev=''
for i in range(-1,-(len(s)+1),-1):
    rev+=s[i]
print(rev)

s=input()
rev=''
ip=-1
while ip>-(len(s)+1):
    rev+=s[ip]
    ip-=1'''

n=int(input())
summ=0

        













