import math
a=float(input("Амплитуда колебания А="))
print("T=2, m=0.2")
t= float(2)
m=float(0.2)
w= (2*math.pow(math.pi, 2)*math.pow(a, 2)*m)/math.pow(t,2)
print("W=(2*π^2*A^2*m)/T^2",w)
input()
