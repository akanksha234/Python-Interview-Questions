# def pair_sum(array, sum):
#     index = 1
#     count = 0
#     list_of_pairs = list()
#
#     if len(array) < 2:
#         return
#
#     for x in array:
#         for y in array[index:]:
#             if ((x + y) == sum and (sorted((x,y)) not in list_of_pairs)):
#                 count += 1
#                 list_of_pairs.append(sorted((x,y)))
#                 break
#         if index != len(array):
#             index += 1
#
#     print()
#     for pair in list_of_pairs:
#         print (pair)
#
#     return count

def pair_sum(array, sum):
    seen = set()
    output = set()
    if len(array) < 2:
        return
    else:
        for num in array:
            target = sum - num
            if target not in seen:
                seen.add(num)
            else:
                output.add((min(num, target), max(num, target)))

        #print out the unique pairs
        print()
        for pair in output:
            print (pair)

        return len(output)





