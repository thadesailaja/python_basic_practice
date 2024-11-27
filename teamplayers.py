class Player():
    def __init__(self,n,a,c,m,w,r):
        self.Pname=n
        self.Page=a
        self.Pcountry=c
        self.Pmatches=m
        self.Pwickets=w
        self.Pruns=r

class Team:
    def __init__(self,n):
        self.nop=n
        self.PL=[]
        for i in range(self.nop):
            n=input('enter player name')
            a=int(input('enter player age'))
            c=input('enter player country')
            m=int(input('enter no of matches'))
            w=int(input('enter wickets'))
            r=int(input('enter no of runs'))
            PO=Player(n,a,c,m,w,r)
            self.PL.append(PO)
