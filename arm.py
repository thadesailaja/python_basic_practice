#armstrong number(153-156)
'''LL=int(input())
UL=int(input())
for n in range(LL,UL+1):
    dummy=n
    l=len(str(n))
    sum=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        sum=sum+rem**l
    if sum==n:
         print(n)'''

#disorder number(175-176)
'''LL=int(input())
UL=int(input())
for n in range(LL,UL+1):
    dummy=n
    l=len(str(n))
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        summ=rem**l
        l-=1
        if summ==n:
            print(n)'''

#special number
'''n=int(input())
summ=0
dummy=n
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    summ+=fact
if summ==n:
    print('n is special')
else:
    print('n is not a special')'''

#special number given range
LL=145
UL=146
for n in range(145,146):
    sum=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        dummy=dummy//10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        sum+=fact
    if sum==n:
        print(n)
