# программа для обработки натуральных чисел

def main():
    intro = ("Программа для определения\n"
                   "Количества цифр в числе n\n"
                   "Суммы цифр в числе n\n"
                   "Первой цифры числа n\n")

    print(intro)
    number = int(input("Введите число n: "))

    a = NumCount(number)
    b = NumSum(number)
    c = NumFirstDigit(number)

    print("Количество цифр в числе n =", a)
    print("Сумма цифр в числе n =", b)
    print("Первая цифра числа n =", c)


# функция подсчета Количество цифр в числе n
def NumCount(n):
    count = 1
    n = n // 10
    while ( n > 0):
        count += 1
        n = n // 10
    return count

# функция подсчета Сумма цифр в числе n
def NumSum(n):
    sum = 0
    while (n != 0) :
        sum += n % 10
        n //= 10
    return sum

# функция подсчета Первая цифра числа n
def NumFirstDigit(n):
    k = n
    while n > 0:
        k = n
        n //= 10
    return k


#вызов функции main
main()