print('Welcome To Mac Donald\'s')

print('Please Select Your Order : ')
print('Menu : ')

i = 1
sum = 0
while i > 0:
    
    print('1. Burger : Rs 250')
    print('2. Fries : Rs 90')
    print('3. Cold Drink : Rs 150')

    i = int(input('Enter Your Item No or (0) to exit! : '))
    if i == 1:
        print('Burger Ordered')
        sum += 250
    elif i == 2:
        print('Fries Ordered')
        sum += 90
    elif i == 3:
        print('Cold Drink Ordered')
        sum += 150
    else:
        break

print('Your Total Bill is : Rs', sum)