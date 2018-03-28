def ff(field):
    f = field
    res = 'D'
    for i in range(3):
        if f[i][0] == f[i][1] and f[i][0] == f[i][2] and f[i][0] != '.':
            res = f[i][0]
        if f[0][i] == f[1][i] and f[0][i] == f[2][i] and f[0][i] != '.':
            res = f[0][i]
    if f[0][0] == f[1][1] and f[0][0] == f[2][2] and f[0][0] != '.':
        res = f[0][0]
    if f[0][2] == f[1][1] and f[0][2] == f[2][0] and f[0][2] != '.':
        res = f[0][2]
    return res

print(ff(["X.O","XX.","XOO"]))