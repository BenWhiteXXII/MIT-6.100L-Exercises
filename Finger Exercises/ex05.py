my_str = str(input('Enter string: '))
str_even = ''
for i in range (0, len(my_str), 2):
        str_even += my_str[i]
print(str_even)
