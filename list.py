#WAP to find sum of digits of agiven list
#the list contain only integers
'''l=int(input('enter list'))
sum=0
for i in l:
    sum+=i
print(sum)'''

##combination of integers and other DT's

'''l=eval(input('enter list:'))
summ=0
for i in l:
    if isinstance(i,int):
        summ+=i
print(summ)'''

##in one line by using sum function
'''l=eval(input('enter list:'))
print(sum(l))'''


#WAP to print max num present in given LIST.
'''L=eval(input('enter list'))
max=0
for i in L:
    if i>max:
        max=i
print(max)


l=eval(input('enter list'))
print(max(l))'''


'''l=eval(input('enter list'))
l.sort()
print(l[-1])'''

#WAP to print abs diff of sum of even num and sum of odd num.
#only integers
'''L=eval(input('enter list'))
es=0
os=0
for i in L:
    k=int(i)
    if int(i)%2==0:
        es+=i
    else:
        os+=i
print(abs(os-es))

#combination of integers and others data types
l=eval(input('enter list'))
es=0
os=0
for i in l:
    if isinstance(i,int):
        k=int(i)
        if int(i)%2==0:
            es=es+i
        else:
            os=os+i
print(abs(es-os))'''


#range
l=int(input('enter list'))
summ=0
for i in range(1,n+1,1):
    summ+=i
print(summ)
