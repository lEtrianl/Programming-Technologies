#def ff(a):
#    c = 0
#    for i in range(a):
#        if i*i == a:
#            c = c + 1
#    if c == 1:
#        return True
#    else:
#        return False
#
#print(ff(4))

def ff(a):
    if (a**0.5) == int(a**0.5):
        return True
    else:
        return False