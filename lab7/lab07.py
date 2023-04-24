LAB_SOURCE_FILE = __file__

this_file = __file__

def skip_add(n):
    """ Принимает число n и возвращает сумму n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Использование циклов запрещено!
    >>> from construct_check import check
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    if n <= 0:
        return 0
    else:
        return n + skip_add(n - 2)



def summation(n, term):
    """Возвращает сумму первых n элементов в поледовательности, заданной term.
    Реализовать с помощью рекурсии!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Использование циклов запрещено!
    >>> from construct_check import check
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n - 1, term)


def paths(m, n):
    """Возвращает число путей из нижнего левого угла сетки M x N с координатами (0, 0)
    в верхний правый (M-1, N-1), используя только сдвиги вправо или вверх.

        finish
          v
    ---------
    | > | o |
    ---------
    | * | ^ |
    ---------
      ^
    start

    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """

    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[0][1] = 1  
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m][n]




def max_subseq(n, t):
    """
    Возвращает максимальную по значению подпоследовательность длины в интервале [1, t],
    которую можно составить из цифр числа n, следуя по слева направо, но не обязательно подряд.
    Например, для n = 20125 и t = 3, такими подпоследовательностями будут:
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    из них наибольшим будет число 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # учтите, что 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # нулевая длина
    0
    >>> max_subseq(12345, 1)
    5
    """
    n_str = str(n)
    

    max_seq = ""
    max_seq_val = -float('inf')
    

    for seq_len in range(1, t+1):
        for start_idx in range(len(n_str) - seq_len + 1):
            seq = n_str[start_idx:start_idx+seq_len]
            seq_val = int(seq)
            if seq_val > max_seq_val:
                max_seq = seq
                max_seq_val = seq_val
    
    return int(max_seq)



def add_chars(w1, w2):
    """
    Необязательное задание.
    Возвращает строку, содержащую символы, недостающие для получения w2 из w1.
    Подразумевается, что w1 - это подпоследовательность w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    >>> from construct_check import check
    >>> # запрещено использовать циклы и множества!
    >>> check(LAB_SOURCE_FILE, 'add_chars',
    ...       ['For', 'While', 'Set', 'SetComp'])
    True
    """
    missing_chars = ""
    for c in w2:
        if c not in w1:
            missing_chars += c
    return missing_chars

