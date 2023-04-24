def falling(n, k):
    """Рассчитать убывающий факториал от n глубины k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    else:
        return n * falling(n - 1, k - 1)

print(falling(6, 3))
print(falling(4, 3))
print(falling(4, 1))
print(falling(4, 0))



def sum_digits(y):
    """Сложить все цифры числа y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123)
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    if y < 10:
        return y
    else:
        return y % 10 + sum_digits(y // 10)

print(sum_digits(10))
print(sum_digits(4224))
print(sum_digits(1234567890))
a = sum_digits(123)
print(a)



def double_eights(n):
    """Возвращает True если в n есть две цифры 8 подряд.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    while n > 0:
        if n % 10 == 8 and n // 10 % 10 == 8:
            return True
        n = n // 10
    return False
    
print(double_eights(8))
print(double_eights(88))
print(double_eights(2882))
print(double_eights(880088))
print(double_eights(12345))
print(double_eights(80808080))
