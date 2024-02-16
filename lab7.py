# ECOR 1041 - Bonus

__author__ = "Emily Causi"
__student_number__ = "101236902"

# ======================================================
# Exercise 1

def replicate(given_String: str) -> str:
    """Return a given string duplicated by a specified amount.
    >>> replicate("abc")
    'abcabcabc'
    >>> replicate("sully")
    'sullysullysullysullysully'
    >>> replicate("pneumonoultramicroscopicsilicovolcanoconiosis")
    'pneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosispneumonoultramicroscopicsilicovolcanoconiosis'
    """
    return given_String * len(given_String)   

# ======================================================
# Exercise 2

def repeat_separator(word: str, sep: str, n: int) -> str:
    """Return a string of word and separating word, of which both are provided, a number of times which is also specified.
    >>> repeat_separator("Word","X",3)
    'WordXWordXWord'
    >>> repeat_separator("This","And",2)
    'ThisAndThis'
    >>> repeat_separator("This","And",1)
    'This'
    """
    i = 0
    fleetwood = word
    while i < n - 1:
        fleetwood += sep + word
        i += 1
    return fleetwood
           
# ======================================================
# Exercise 3

def has_pair(s: str, ch: str) -> bool:
    """Return whether or not a provided word contains 2 instances of specified characters beside one another.
    >>> has_pair('abccd', 'c')
    True
    >>> has_pair('abcdc', 'c')
    False
    >>> has_pair('abbbcd', 'b')
    True
    """
    for character in range(len(s) - 1):
        if (s[character] == ch and s[character + 1] == ch):
            return True
    return False

# ======================================================
# Exercise 4

def middle_way(a: list[int], b: list[int]) -> list:
    """Return the middle characters from two provided strings.
    Parameters: len(a) == 3,
    len(b) == 3
    >>> middle_way([1, 2, 3], [4, 5, 6])
    (2, 5)
    >>> middle_way([3, 7, 0], [2, 8, 1])
    (7, 8)
    >>> middle_way([2, 2, 2], [4, 9, 0])
    (2, 9)
    """
    return a[1], b[1]

# ======================================================
# Exercise 5

def make_ends(a: list[int]) -> list:
    """Return the first and last characters of a provided string.
    >>> make_ends([4,5,6,7])
    (4, 7)
    >>> make_ends([-2,8,4,0])
    (-2, 0)
    >>> make_ends([1,4,2,1])
    (1, 1)
    """
    return a[0], a[len(a)-1]

# ======================================================
# Exercise 6

def common_end(a: list[int], b: list[int]) -> bool:
    """Return whether or not the first or last characters in the given strings are the same values.
    >>> common_end([9, 2, 6], [8, 7, 9])
    True
    >>> common_end([0, 2, 0], [8, 0, 1])
    False
    >>> common_end([2, 6, 6], [2, 1, 2])
    True
    """
    return (a[0] == b[0] or a[len(a)-1] == b[len(b)-1] or a[0] == b[len(b)-1] 
            or b[0] == a[len(a)-1])

# ======================================================
# Exercise 7

def count_evens(a: list[int]) -> int:
    """Return the number of even values in a provided list.
    >>> count_evens([3,5,6,2,8])
    3
    >>> count_evens([2,4,4,8])
    4
    >>> count_evens([6,3,1,0,4])
    3
    """
    count = 0
    for i in range(len(a)):
        if (a[i] % 2 == 0):
            count += 1
    return count
    
# ======================================================
# Exercise 8

def big_diff(a: list[int]) -> int:
    """Return the difference between the greatest and the least values in a provided list.
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([20, 5, 7, 1])
    19
    >>> big_diff([2, 8, -4, 7])
    12
    """
    max_Value = max(a)
    min_Value = min(a)
    for elem in a:
        if elem > max_Value:
            elem = max_Value
        elif elem < min_Value:
            elem = min_Value
    return max_Value - min_Value
    
# ======================================================
# Exercise 9

def has22(a: list[int]) -> bool:
    """ Return true if two 2s appear beside one another in a provided list.
    >>> has22([4, 2, 3, 2])
    False
    >>> has22([1, 2, 2, 3])
    True
    >>> has22([2, 1, 2, 4])
    False
    """
    for i in range(len(a)-1):
        if (a[i] == 2 and a[i+1] == 2):
            return True
    return False

# ======================================================
# Exercise 10

def centered_average(a: list[int]) -> bool:
    """Return the arithmetic mean of the numbers of a provided list, without the largest and smallest values, unless they appear more than once.
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5.2
    >>> centered_average([2, 9, 6, 3, 3, 2, 9])
    4.6
    >>> centered_average([0, 12, 6, 1, 1])
    2.67
    """
    max_Value = max(a)
    min_Value = min(a)
    count = 0
    for i in range (len(a)):
        if a[i] > max_Value:
            max_Value = a[i]
        elif a[i] < min_Value:
            min_Value = a[i]
        count += a[i]
    count -= max_Value + min_Value
    return round(count / (len(a) - 2),2)

# ======================================================
# Exercise 11

def bank_statement(a: list[float]) -> list:
    """Return the sum of deposits, withdrawls, and current balance in a bank account.
    <<< bank_statement([12.47, -47.82, 80.23, -2.33, 9.82])
    (102.52, -50.15, 152.67)
    <<< bank_statement([90.25, -12.32, 70.28, 2.80, 20.07, -60.55])
    (183.4, -72.87, 256.27)
    <<< bank_statement([100.03, -40.59, -4.06, 80.67])
    (180.7, -44.65, 225.35)
    """
    deposits = 0
    withdrawls = 0
    for i in range(len(a)):
        if a[i] >= 0:
            deposits += a[i]
        else:
            withdrawls += a[i]
    return round(deposits,2), round(withdrawls,2), round(deposits - withdrawls,2)

# ======================================================
# Exercise 12

def reverse(a: list) -> list:
    """Return a list in the reversed order, provided it is not empty.
    >>> reverse([4, 2, 3, 2])
    [2, 3, 2, 4]
    >>> reverse([0, 2, 6, 8])
    [8, 6, 2, 0]
    >>> reverse([3, 3, 7, 3])
    [3, 7, 3, 3]
    """
    return [a[-(i+1)] for i in range(len(a))]
