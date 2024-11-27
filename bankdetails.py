class bank_v1():
    bank_name='sbi'
    bank_roi=6
    bank_ifsc=1245
    bank_address='kizikisthan'
    def __init__(self,n,ac,b,ad):
        self.cname=n
        self.caccount=ac
        self.cbalance=b
        self.caddress=ad

    def customer_details(self):
        print(f'name of the customer {self.cname}')
        print(f'account of the customer {self.caccount}')
        print(f'balance of the customer {self.cbalance}')
        print(f'address of the customer {self.caddress}')


    @staticmethod
    def get_int_value():
        value=int(input('enter int value'))
        return value
    def withdraw(self):
        amount=self.get_int_value()
        if amount<=self.cbalance:
            self.cbalance-=amount
            print('withdraw is successfull')
        else:
            print('insufficient is successfull')

    def deposite(self):
        amount=self.get_int_value()
        if amount>0:
            self.cbalance+=amount
            print('deposite is successfull')
        else:
            print('amount should be more than one re')

class bank_v2(bank_v1):
    bank_address='banglore'
    bank_mobile=8897638923

    @classmethod
    def bank_details(cls):
        print(f'bank name is {cls.bank_name}')
        print(f'bank roi is {cls.bank_roi}')
        print(f'bank ifsc is {cls.bank_ifsc}')
        print(f'bank address is {cls.bank_address}')
        print(f'bank monbile number is {cls.bank_mobile}')

    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_value()
        cls.bank_roi=newroi
        print('roi is changed')

sailaja=bank_v2('sailu',1234,56564,'banglore')
sailaja.customer_details()
bank_v2.bank_details()
bank_v1.newroi()















        

