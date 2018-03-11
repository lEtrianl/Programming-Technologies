rub = 1
dollar = 56.3
euro = 68.67
uan = 8.9
griv = 2.1
yen = 0.52

v = [rub, dollar, euro, uan, griv, yen]
t = ['в рублях', 'в долларах', 'в евро', 'в юанях', 'в гривнах', 'в йенах']


def convert(money, ind):
    return [t[ind], str(round(money / v[ind], 2))]
