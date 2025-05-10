name = 'xyze'
name = "xyze"
name = '''xyze'''
name = """xyze"""

print(name) # xyz

# Accessing Characters from String
print('\nFirst Char : ',name[0]) # x
print('Second Char : ',name[1]) # y
print('Last Char : ',name[-1]) # e


# Length of String
print('\nLength : ',len(name)) # 4

# String Slicing
print('\nSlicing String :',name[0:5]) # xy
print('Slicing String :',name[:2]) # xyz
print('Slicing String :',name[2:]) # ze


# String Concatenation
name1 = 'xyz'
name2 = 'abc'
name3 = name1 + name2
print('\nConcatenation : ',name3) # xyzabc

# String Repetition
name = 'xyz'
name = name * 3
print('\nRepetition : ',name) # xyzxyzxyz

# String Transformation
# Lowercase
name = 'XYZ'
name = name.lower()
print('\nLowercase : ',name) # xyz

# Uppercase
name = 'xyz'
name = name.upper()
print('\nUppercase : ',name) # XYZ

# Titlecase
name = 'xyz abc'
name = name.title()
print('\nTitlecase : ',name) # Xyz Abc

# Capitalize
name = 'xyz abc'
name = name.capitalize()
print('\nCapitalize : ',name) # Xyz abc

# Swapcase
name = 'xyz ABC'
name = name.swapcase()
print('\nSwapcase : ',name) # XYZ abc

# String Stripping
name = '\n\n\n\n\n\n   xyz   '
name = name.strip()
print('\nStrip : ',name) # xyz


# String Replacing
name = 'xyz abc'
name = name.replace('abc','123')
print('\nReplace : ',name) # xyz 123


'''-------------------------------------------------------------------'''

# String Splitting
name = 'xyz abc'
name = name.split(' ')
print('\nSplit : ',name) # ['xyz', 'abc']

# String Joining
name = ['xyz', 'abc']
name = ' '.join(name)
print('\nJoin : ',name) # xyz abc

# String Formatting
name = 'xyz'
age = 20
name = f'{name} is {age} years old'
print('\nFormat : ',name) # xyz is 20 years old

# String Formatting with format()
name = 'xyz'
age = 20
name = '{} is {} years old'.format(name, age)
print('\nFormat : ',name) # xyz is 20 years old e4rl5t6789


# String Formatting with % operator
name = 'xyz'
age = 20
name = '%s is %d years old' % (name, age)
print('\nFormat : ',name) # xyz is 20 years old

