import math
c=float(math.pow(10,-6))
l=float(0.04)
u=float(100)
print("C=10^(-6)Ф")
print("L=",l,"Гн")
print("U=",u,"B")
i=u*math.sqrt(c/l)
print("I=",i,"A")
W=(l*math.pow(i,2))/2
print("W=",W,"Дж")



