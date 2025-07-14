s=input("Enter a lowercase string: ")
a=""
for i in s:
    if i not in a:
        a+=i

print(len(a))
