from continuous_sum import largest_continuous_sum

def test_1():
    assert(largest_continuous_sum([1, 2, -1, 3, 4, -1])== 9)
def test_2():
    assert(largest_continuous_sum([1, 2, -1, 3, 4, 10, 10, -10, -1])== 29)
def test_3():
    assert(largest_continuous_sum([-1, 1])== 1)
