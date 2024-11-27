'''class Employee:
    cname='google'
    caddress='marathahalli'
    empCount=0

    def __int__(self,n,i,s):
        self.ename=n
        self.eid=i
        self.esal=s
        Employee.empCount+=1

    def __del__(self):
        Employee.empCount-=1
        print(f'{self} object is deleted')
        
abc=Employee('abc',234,20000)

print(abc.empCount)
print(Employee.empCount)


class Book:
    def __init__(self,n,a,p):
        self.Bname=n
        self.Bauthor=a
        self.Bprice=p

    def __str__(self):
        return str(self.Bprice)
    

    def __del__(self):
        print('object is deleted')
        


python=Book('python','van guido rossum',1000)
django=Book('django','simon willison',20000)
print(django)
#del django
django=None'''


'''class Book:
    def __init__(self,n,a,p):
        self.Bname=n
        self.Bauthor=a
        self.Bprice=p
    def __str__(self):
        return self.Bname

    def __add__(self,other):
        return self.Bprice+other.Bprice

    def __sub__(self,other):
        amount=self.Bprice-other.Bprice
        if amount>=0:
            print('shopkeeper wiil return the amount to the customer')
        else:
            print('customer wiil give the remaining amount to the shope keeper')
        #return self.Bprice-other.Bprice
    def __mul__(self,value):
        return self.Bprice*value
    
python=Book('python','van guido rossum',10000)
django=Book('django','simon willison',20000)
print(django)
print(python+django)
print(django-python)
print(python-django)
print(django*3)


class Rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def __gt__(self,other):
        area1=self.length*other.breadth
        area2=self.breadth*other.length

        return True if area1>area2 else False

R1=Rectangle(1000,400)
R2=Rectangle(5000,1800)
print(R1>R2)'''

from abc import ABC,abstractmethod

class TimeTable(ABC):
    @abstractmethod
    def javascript(self):
        pass
    @abstractmethod
    def python(self):
        pass
    @abstractmethod
    def presentation(self):
        pass

class sailaja(TimeTable):
    def javascript(self):
        print('javascript class timing 7:30am to 9:30am')

    def python(self):
        print('python class timing 11:30am to 1:30pm')

    def presentation(self):
        print('presentation class timing 5:00pm to 6:00pm')

s=sailaja()
s.javascript()
s.python()
s.presentation()
    
