from pairs_with_sum import pair_sum


def test_1():
    assert(pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)== 6)
def test_2():
    assert(pair_sum([1, 2, 3, 1], 3)== 1)
def test_3():
    assert(pair_sum([1, 3, 2, 2], 4)== 2)