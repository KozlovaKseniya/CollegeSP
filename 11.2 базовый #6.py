t=float(input('Time: '))
u=float(input('Speed: '))
class Rod:
    def __init__(self,time):
        self.t=time
class Det(Rod):
    def __init__(self, time,speed):
        Rod.__init__(self, time)
        self.u=speed
    def rast(self):
        self.s=self.t*self.u
    def out(self):
        print('Пройденное расстояние: ', self.s)
moto=Det(t,u)
moto.rast()
moto.out()
    
        
    
    
