# for loop with collection--->
''' it is used whenever we want to extract each and every element from the collection directly'''
'''  for variable in CDT:
             statements of
               for loop'''


s=input('enter string')
c=0
for i in s:
    c+=1
print(c)

s=input('enter string')
s1=input('enter substr')
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
    if i not in v:
        c+=1
print(c)


s=input('enter string')
v='aeiouAEIOU'
c=0
for i in s:
    if i.isalpha() and i not in v:
        c=c+1
print(c)


s=input('enter string')
v='aeiouAEIOU'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc=vc+1
        else:
            cc=cc+1
print(vc)
print(cc)

s=input('enter string:')
c=0
for i in s:
    if i.isdigit():
        c=c+1
print(c)

s=input('enter string:')
sum=0
for i in s:
    if i.isdigit():
        k=int(i)
        sum+=k
print(sum)

s=input('enter string:')
es=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
print(es)

s=input('enter string:')
es=0
os=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
        else:
            os+=k
print(abs(es-os))


s=input('enter string:')
c=0
for i in s:
    if not i.isalnum():
        c=c+1
print(c)
        




