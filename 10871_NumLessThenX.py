n, x = map(int, input().split())

# Read N integers into the list 'a'
a = list(map(int, input().split()))

# Create an empty list
ans = []

# Iterate through each number in 'a'
for i in a:
    if i < x:          # if the number is less than X
        ans.append(i)  # Add the number to 'ans' list

# Print all in 'ans', separated by spaces -> print(*array)
print(*ans)
