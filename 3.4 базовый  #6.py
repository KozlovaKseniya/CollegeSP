import math
x=1.0
while x<3.1:
    y=math.pow(x,3)-4*math.pow(x,2)+2
    print (round(x,1), "\t", round(y,3))
    x=x+0.2
