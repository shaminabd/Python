#Cramer's Rule
import time

start = time.time()



print("Enter the coeffecients in the following format")
print("a1x + b1y + c1z = d1 ")
print("a2x + b2y + c2z = d2 ")
print("a3x + b3y + c3z = d3 ")

a1=float(input('Enter a1: '))
b1=float(input('Enter b1: '))
c1=float(input('Enter c1: '))
d1=float(input('Enter d1: '))
a2=float(input('Enter a2: '))
b2=float(input('Enter b2: '))
c2=float(input('Enter c2: '))
d2=float(input('Enter d2: '))
a3=float(input('Enter a3: '))
b3=float(input('Enter b3: '))
c3=float(input('Enter c3: '))
d3=float(input('Enter d3: '))

print("The equations entered are")
print(a1,"x + ",b1,"y + ",c1,"z = ",d1)
print(a2,"x + ",b2,"y + ",c2,"z = ",d2)
print(a3,"x + ",b3,"y + ",c3,"z = ",d3)

D = a1*(b2*c3-b3*c2)-b1*(a2*c3-a3*c2)+c1*(a2*b3-a3*b2)
if D==0:
    print("The determinant of the coefficient matrix is zero, Cramer's Rule cannot be applied")
else:
    x=(d1*(b2*c3-c2*b3)-b1*(d2*c3-d3*c2)+c1*(d2*b3-b2*d2))/D
    y=(a1*(d2*c3-d3*c2)-d1*(a2*c3-c2*a3)+c1*(a2*d3-d2*a3))/D
    z=(a1*(b2*d3-d2*b3)-b1*(a2*d3-d2*a3)+d1*(a2*b3-a3*b2))/D

    print("Solutions by using Cramer's Rule are")
    print('x= ',x,' y= ',y,' z= ',z)

end = time.time()
print(round((end - start), 2), "s seconds were spent to process this program" )

range