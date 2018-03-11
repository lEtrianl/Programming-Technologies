import conv
import account

def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money, period)
    for i in range(len(conv.v)):
        m = conv.convert(money, i)
        r = conv.convert(result, i)
        print("Параметры счета ({0}):\n".format(m[0]), "Сумма ({0}): {1}".format(m[0], m[1]), "\n", "Ставка: ", rate,
              "\n", "Период: ", period, "\n", "Сумма на счете в конце периода ({0}): {1}".format(r[0], r[1]))


main()

