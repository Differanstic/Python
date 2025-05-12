i : int
j : float
k : str
l : bool
m : None
# Python Data Types

i = 5
j = 3.14
k = 'abc'
l = True
m = None

print(type(i))  # <class 'int'>
print(type(j))  # <class 'float'>
print(type(k))  # <class 'str'>
print(type(l))  # <class 'bool'>
print(type(m))  # <class 'NoneType'>

# Type Conversion
# int to float
i = 5
j = float(i)
print(j)  # 5.0

# float to int
j = 3.14
i = int(j)
print(i)  # 3

# str to int
i = '5'
j = int(i)
print(j)  # 5

# str to float
i = '3.14'
j = float(i)
print(j)  # 3.14

# int to str
i = 5
j = str(i)
print(j)  # '5'

# float to str
i = 3.14
j = str(i)
print(j)  # '3.14'

# bool to int
i = True
j = int(i)
print(j)  # 1

# bool to str
i = True
j = str(i)
print(j)  # 'True'

