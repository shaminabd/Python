def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res += v
   return res
string=input()
lst=string.split()
print("",lst)