'''n=int(input())
summ=0
for i in range(1,n//2+1):
    if n%i==0:
        summ+=i
if n==summ:
    print('n is a perfect number')
else:
    print('n is not a petfect')'''

'''n=int(input())
sum=0
i=1
while i<=n//2:
    if n%i==0:
        sum+=i
        i+=1
if n==sum:
    print('n is a perfect number')
else:
    print('n is not a perfect number')'''

c=int(input())
sum=0
pc=0
n=1
while True:
    if n<=n//2:
        for i in range(1,n//2+1):
            if n%i==0:
                sum+=1
                break
        else:
            n+=1
            pc+=1
            
    if n==sum:
        print('perfect')
        break 
        '''else:
            pc+=1'''
'''if n==sum:
 print('n is perfect number')'''
n+=1
                
    
