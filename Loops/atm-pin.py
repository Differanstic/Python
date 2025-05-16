pin = 123456
i = 1

# break
while  i <= 3:
    user_pin = int(input('Enter pin : '))
    
    if user_pin == pin :
        print('Access granted')
        break
        
    else :
        print('Incorrect Pin\nTriese Remaining : ',3-i)
    
    
    i = i +1
    