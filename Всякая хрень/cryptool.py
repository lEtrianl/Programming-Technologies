def ff(cryp):
    k = {}
    st = cryp.lower()
    for i in st:
        if i in list(k.keys()):
            k[i] += 1
        else:
            k[i] = 1
    return k

print(ff("Hello"))