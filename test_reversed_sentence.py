from sentence_reversal import reverse_sentence


def test_1():
    assert(reverse_sentence('    space before')== 'before space')

def test_2():
    assert(reverse_sentence('space after     ')== 'after space')

def test_3():
    assert(reverse_sentence('   Hello John    how are you   ')== 'you are how John Hello')

def test_4():
    assert(reverse_sentence('1')== '1')
