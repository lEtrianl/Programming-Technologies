def ff(str1, str2):
    st1, st2 = str1.lower(), str2.lower()
    k1, k2 = {}, {}
    for i in st1:
        if i in list(k1.keys()):
            k1[i]+=1
        else:
            k1[i]=1
    for i in st2:
        if i in list(k2.keys()):
            k2[i]+=1
        else:
            k2[i]=1
    if ' ' in k1.keys():
        del(k1[' '])
    if ' ' in k2.keys():
        del(k2[' '])
    if k1 == k2:
        return True
    else:
        return False

print(ff("Programming", "Gram Ring Mop"))
print(ff("Hello", "Ole Oh"))
print(ff("Kyoto", "Tokyo"))