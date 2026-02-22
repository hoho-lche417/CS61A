SOURCE_FILE = __file__


def print_if(s, f):
    """Print each element of s for which f returns a true value.

    >>> print_if([3, 4, 5, 6], lambda x: x > 4)
    5
    6
    >>> result = print_if([3, 4, 5, 6], lambda x: x % 2 == 0)
    4
    6
    >>> print(result)  # print_if should return None
    None
    """
    for x in s:
        if f(x):
            print(x)


def close(s: list[int], k: int) -> int:
    """Return how many elements of s are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    assert k >= 0
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        if abs(i - s[i]) <= k:
            count += 1
    return count


def close_list(s: list[int], k: int) -> list[int]:
    """Return a list of the elements of s that are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close_list(t, 0)  # Only 3 is equal to its index
    [3]
    >>> close_list(t, 1)  # 2, 3, and 5 are within 1 of their index
    [2, 3, 5]
    >>> close_list(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    [2, 4, 3, 5]
    """
    assert k >= 0
    return [s[i] for i in range(len(s)) if abs(s[i] - i) <= k]


from math import sqrt

def squares(s: list[int]) -> list[int]:
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [int(sqrt(n)) for n in s if sqrt(n) == round(sqrt(n))]


def double_eights(n: int) -> bool:
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration, in operator and str function 
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'double_eights', ['While', 'For', 'In', 'Str'])
    True
    """
    
    if n < 10:
        return False
    return n % 10 == 8 and n // 10 % 10 == 8 or double_eights(n // 10)


def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return False
        elif x == y:
            return True
        else:
            return can_reach(f(x), y, limit - 1) or can_reach(g(x), y, limit - 1)
    return can_reach


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952) # 7+3, 8+2, and 8+2
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469) # 9+1, 6+4, 6+4, 4+6, 1+9, 4+6 
    6
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'ten_pairs', ['While', 'For'])
    True
    """

    if n < 10:
        return 0    
    return count_digit(n // 10, 10 - n % 10) + ten_pairs(n // 10)


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5) # digit 5 appears 4 times in 55055
    4
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(SOURCE_FILE, 'count_digits', ['While', 'For'])
    True
    """

    if n == 0:
        return 0
    return int(n % 10 == digit) + count_digit(n // 10, digit)





## from discussion

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):
        result = result + [ [k] + rest for rest in sums(n - k, m) if rest == [] or rest[0] != k ]
    return result

# print(sums(6, 3))
# sums(5, 2)
# sums(5, 3)
# sums(5, 5)
# sums(6, 3)


def fit(total, n):
    """Return whether there are n positive perfect squares that sums to total.

    >>> [fit(4, 1), fit(4, 2), fit(4, 3), fit(4, 4)]  # 1*(2*2) for n=1; 4*(1*1) for n=4
    [True, False, False, True]
    >>> [fit(12, n) for n in range(3, 8)]  # 3*(2*2), 3*(1*1)+3*3, 4*(1*1)+2*(2*2)
    [True, True, False, True, False]
    >>> [fit(32, 2), fit(32, 3), fit(32, 4), fit(32, 5)] # 2*(4*4), 3*(1*1)+2*2+5*5
    [True, False, False, True]
    """
    def f(total, n, k):
        if total == k * k:
            #return True
            return n == 1
        elif total < k * k:
            return False
        else:
            b1 = f(total - k*k, n - 1, k)
            b2 = f(total - k*k, n - 1, k + 1)
            b3 = f(total, n, k + 1)
            res = n > 0 and (b1 or b2 or b3)
            return res
            # return n > 0 and (f(total - k*k, n - 1, k) or f(total - k*k, n - 1, k + 1) or f(total, n, k + 1))
    return f(total, n, 1)

print([fit(4, 1), fit(4, 2), fit(4, 3), fit(4, 4)])
print([fit(12, n) for n in range(3, 8)])
print([fit(32, 2), fit(32, 3), fit(32, 4), fit(32, 5)])

# print(fit(4, 2))

def f(total, n, k):
    if total == k * k:
        #return True
        return n == 1
    elif total < k * k:
        return False
    else:
        b1 = f(total - k*k, n - 1, k)
        b2 = f(total - k*k, n - 1, k + 1)
        b3 = f(total, n, k + 1)
        res = n > 0 and (b1 or b2 or b3)
        return res
        # return n > 0 and (f(total - k*k, n - 1, k) or f(total - k*k, n - 1, k + 1) or f(total, n, k + 1))

#print(f(4, 2, 2)) # should be false but returns true
