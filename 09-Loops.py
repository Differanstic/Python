# Loops
# Loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or to repeat a block of code multiple times.
# There are two main types of loops in Python:
# 1. for loop
# 2. while loop

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count by 1
    
# break statement
count = 0
while count < 5:
    if count == 3:
        break  # Exit the loop when count is 3
    print(count)
    count += 1  # Increment count by 1




# For Loop
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for char in string.lower():
    print(char)


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Using range() with for loop
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
    
# Using range() with start and end
for i in range(2, 10):
    print(i)  # 2, 3, 4, 5, 6, 7, 8, 9
    
# Using range() with start, end, and step
for i in range(2, 10, 2):
    print(i)  # 2, 4, 6, 8
    


# Using break statement
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # 0, 1, 2, 3, 4