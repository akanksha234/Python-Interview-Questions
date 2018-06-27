def largest_continuous_sum(arr):
    if len(arr) == 2:
        maximum_sum = max(arr)
        print("\n Maximum sum is {0} with starting and ending point as {0}".format(maximum_sum))
        return maximum_sum
    else:
        current_sum = maximum_sum = arr[0]
        starting_point = current_sum
        for number in arr[1:]:
            current_sum += number
            if current_sum > maximum_sum:
                maximum_sum = current_sum
                ending_point = number

        print("\n Maximum sum is {0} with starting point as {1} and ending point as {2}.".format(maximum_sum, starting_point, ending_point))
        return maximum_sum
