def finder(array1, array2):

    num  = 0
    for n in array1:
        num += n
    for n in array2:
        num -= n

    print("{0} is missing from second array.".format(num))

    return num
