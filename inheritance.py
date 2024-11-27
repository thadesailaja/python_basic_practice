class A:
    house='IBHK'
    bike='HONDA'
class B(A):
    bike='KTM'
    money=12345

OA=A()
OB=B()

print(A.bike)
print(B.bike)
print(B.house)

#Modifying parent class properties by using parent class
'''A.house='2BHK'
print(A.house)
print(OA.house)
print(B.house)
print(OB.house)'''


#Modifying parent object class properties by using parent class
OA.house='2BHK'
print(A.house)
print(OA.house)
print(B.house)
print(OB.house)

#Modifying child class properties by using child class
'''B.house='2BHK'
print(A.house)
print(OA.house)
print(B.house)
print(OB.house)'''


#Modifying child object properties by using child class
'''OB.house='2BHK'
print(A.house)
print(OA.house)
print(B.house)
print(OB.house)'''
