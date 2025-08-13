# Read 9 integers from input and store them in a list 'x'
# Using list comprehension: repeats int(input()) 9 times
# in for, "_" means ignore. For usage only repeat count.(9)
x = [int(input()) for _ in range(9)]

max_num = max(x)

print(max_num)

# Find the index of the maximum value (0-based index)
# Add 1 to convert it to 1-based index as required by the problem
print(x.index(max_num) + 1)
