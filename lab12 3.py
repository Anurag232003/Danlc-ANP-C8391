
tuples_list = [(1, 2), (3, 4), (5, 6)]

total_sum = sum(sum(t) for t in tuples_list)

print("Sum of numbers in the given tuple of tuples:", total_sum)
