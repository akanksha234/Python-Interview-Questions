from anagram import anagram

def test_ana_1():
    assert(anagram("google", "googly"))
def test_ana_2():
    assert(anagram("amazing","zingama"))
def test_ana_3():
    assert(anagram("public relations","crap built on lies"))
def test_ana_4():
    assert(anagram("clint eastwood","old west action"))


