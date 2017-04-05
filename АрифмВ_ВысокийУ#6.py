import math
print("K=((x+b-a)^(1/2)+ln(y))/arctg(b+a)")
x=float(input("x="))
y=float(input("y="))
a=float(input("a="))
b=float(input("b="))
k=(math.sqrt(x+b-a)+math.log(y))/math.atan(b+a)
print("K=",k)
        
