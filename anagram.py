def anagram(s1, s2):
    # arr1 = list(s1)
    # arr2 = s2.split()
    length = 0
    s1 = s1.replace(' ','')
    s2 = s2.replace(' ','')

    for x in s1:
        if x in s2:
            index = s2.index(x)
            s2 = s2[:index]+ s2[index+1:]
            length += 1
            

    if length == len(s1):
        return True
    else:
        return False



if __name__ == "__main__":
    is_anagram = anagram("god", "dog")
    if is_anagram:
        print("Yay! you have got an anagram.")
    else:
        print("Sadly! this is not an anagram.")







