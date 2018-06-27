from find_missing_element import finder

def test_1():
    assert(finder([5, 5, 7, 7], [5, 7, 7])== 5)
def test_2():
    assert(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])== 5)
def test_3():
    assert(finder([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1])== 6)