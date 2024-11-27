##FOR LOOP WITH CDT(str,list,tuple,set,dic)-->>

s=input('enter string:')
s1=input('enter sub string:')
for i in s1:
    print('enter for loop')
    print(i)


l=[1,2,3,4,['hello',25]]
for k in l:
    print(k)


l=int(input('enter list'))
for i in l:
    print(i)


t=(11,22,33,['hello',89])
for i in t:
    print(i)

s={11,22,33,('hello',45)}
for i in s:
    print(i)

d={'name':'sailu','age':23}
for k in d:
    print(k,d[k])

d={'name':'sailu','age':23}
for k,v in d.items():
    print(k,v)

#FOR LOOP WITH CDT(STRING)--->

#WAP to check how many elements are present in given string
S=input('enter string:')
c=0
for i in S:
    c+=1
print(c)


#WAP to find HWT the given substr is present in a str
S1=input('enter string:')
s2=input('enter substr:')
c=0
for i in S1:
    if i==s2:
        c+=1
print(c)

#WAP to print HM vowels are present in a str
s=input('enter string')
v='aeiouAEIOU'
c=0
for i in s:
    if i in v:
        c=c+1
print(c)

#WAP to print HW consonents are present in astr
s=input('enter string:')
v='aeiouAEIOU'
c=0
for i in s:
    if i.isalpha() and i not in v:
        c=c+1
print(c)

#WAP to print HM V's & C's are present in a str
s=input('enter string:')
v='aeiouAEIOU'
vc=0
cv=0
for i in s:
    if i.isalpha():
        if i in v:
            vc=vc+1
        else:
            cv=cv+1
print(f'vowels count is {vc}')
print(f'consonents count is {cv}')


#WAP to print HMI are present in str
s=input('enter string:')
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)


#print the sum of integers present in a given str
s=input('enter string:')
summ=0
for i in s:
    if i.isdigit():
        k=int(i)
        summ+=k
print(summ)
    
    
#WAP to print sum of even digits present in a str
s=input('enter string:')
summ=0
for i in s:
    if i.isdigit():
        k=int(i)
        if int(i)%2==0:
            summ=summ+k
print(summ)

#WAP to print abs diff b/w sum of E & O digits present in a given str
s=input('enter string:')
es=0
os=0
for i in s:
    if i.isdigit():
        k=int(i)
        if int(i)%2==0:
            es+=k
        else:
            os+=k
print(abs(os-es))


#WAP to print HM special charecters present in a str
s=input('enter string:')
c=0
for i in s:
    if not i.isalnum():
        c=c+1
print(c)


#FOR LOOP WITH CDT(LIST)--->

#WAP to find sum of digits of a given list
l=input('enter list:')
summ=0
for i in l:
    summ+=1
print(summ)

#combination of int & other DT!
l=eval(input('enter list:'))
summ=0
for i in l:
    if isinstance(i,int):#isinstance(data,data type)
        summ+=i
print(summ)

l=eval(input('enter list:'))#only integers
print(sum(l))

#WAP to print max num present in given list
l=eval(input('enter list:'))
max=0
for i in l:
    if i>max:
        max=i
print(max)

#WAP abs diff b/w sum of E & O numbers
l=eval(input('enter list'))
es=0
os=0
for i in l:
    if i%2==0:
        es+=i
    else:
        os+=i
print(abs(es-os))



