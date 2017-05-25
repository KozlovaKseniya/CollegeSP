h=int(input('Часы: '))
m=int(input('Минуты: '))
s=int(input('Секунды: '))
class Time:
    def __init__(self,x,y,z):
        self.h=x
        self.m=y
        self.s=z
    def mid(self):
        self.night=24*60-(24*self.h+self.m+self.s/60)
    def addmin(self):
        self.am=self.m+100
    def out(self):
        print('Количество минут до полуночи: ',self.night)
        print('Время увеличили на 100 минут: Часы ',self.h,'Минуты ',self.am,'Секунды ',self.s)
    def __del__(self):
        print()
times=Time(h,m,s)
times.mid()
times.addmin()
times.out()
del Time
        
            
            
        
