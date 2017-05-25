m=int(input('Количество минут: '))
s=int(input('Количество секунд: '))
class myclass:
    def __init__(self,p1,p2):
        self.m=p1
        self.s=p2
    def obrabotka(self):
        self.ob=self.m*60+self.s
    def stroka(self):
        print('Общее количество секунд: ',self.ob)
d=myclass(m,s)
d.obrabotka()
d.stroka()


        
    
