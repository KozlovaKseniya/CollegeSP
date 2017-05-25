import math
x1=float(input('Введите x1: '))
y1=float(input('Введите y1: '))
x2=float(input('Введите x2: '))
y2=float(input('Введите y2: '))
color=str(input('Цвет линий: '))
class Rod:
    def __init__(self,a1,b1,a2,b2):
        self.x1=a1
        self.x2=a2
        self.y1=b1
        self.y2=b2
class Kv(Rod):
    def __init__(self,col,a1,b1,a2,b2):
        Rod.__init__(self,a1,b1,a2,b2)
        self.color=col
    def plo(self):
        self.pp=(math.fabs(self.x1-self.x2)+math.sqrt(math.pow((self.x1-self.x2),2)+math.pow((self.y1+self.y2),2)))/2
        self.a=self.pp-math.fabs(self.x1-self.x2)
        self.b=self.pp*2-(math.sqrt(math.pow((self.x1-self.x2),2)+math.pow((self.y1+self.y2),2)))/2                 
        self.plos=math.sqrt(self.pp*(self.pp-self.a)*math.pow((self.pp-self.b),2))
        print('Площадь наддиагонального треугольника: ',self.plos)
Kvadrat=Kv(color,x1,y1,x2,y2)
Kvadrat.plo()                          
                          
                                   

    
