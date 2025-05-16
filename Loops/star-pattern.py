import time
c = input("Enter star: ")
n = int(input("Enter a number: "))
i = 0

while i < n :
    j = 0
    while j <= i :
        print(c, end=" ")
        j += 1
    print('')
    time.sleep(0.2)
    i += 1
    
# The above code prints a right-angled triangle pattern of stars.


# Reserving Star Pattern

while i >= 0 :
    j = 0
    while j <= i :
        print(c, end=" ")
        j += 1
    print('')
    time.sleep(0.2)
    i -= 1