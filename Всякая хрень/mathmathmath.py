import math
#
#def ff(a,b):
#    c = math.sin(a)
#    d = math.factorial(b)
#    while a != 0 and b != 0:
#        if a > b:
#            a = a % b
#        else:
#            b = b % a
#    return round(((c*(a+b))**d), 2)
#
#print(ff(-1,3))
#print(ff(4,2))
#print(ff(3,3))

#import math
#
#def ff(a,b):
#    c = math.sin(a)
#    f = 1
#    i = 0
#    while i < b:
#        i+=1
#        f = f*i
#    while a != 0 and b != 0:
#        if a > b:
#            a = a % b
#        else:
#            b = b % a
#    return round(((c*(a+b))**f), 2)
#
#print(ff(-1,3))
#print(ff(4,2))
#print(ff(3,3))

def ff(a,b):
    c = math.sin(a)
    d = math.factorial(b)
    f = math.gcd(a,b)

    return round(((c*f)**d),2)

print(ff(-1,3))
print(ff(4,2))
print(ff(3,3))