name=str(input('Марка: '))
value=float(input('Цена: '))
ob=float(input('Объем: '))
p=int(input('Кол-во Sim карт: '))
class Phone:
    def __init__(self,a,b,c):
        self.name=a
        self.value=b
        self.ob=c
    def ka(self):
        self.Q=self.ob/self.value
    def out(self):
        print('Q = ',self.Q)
class Phone2:
    def __init__(self,a,b,c,d):
        Phone.__init__(self,a,b,c)
        self.p=d
    def ka(self):
        Phone.ka(self)
        self.qp=self.Q*self.p
    def out(self):
        print('Qp = ',self.qp)
mobile=Phone2(name,value,ob,p)
mobile.ka()
mobile.out()
            
