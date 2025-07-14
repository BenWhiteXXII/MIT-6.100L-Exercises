snum=1
found=False
for i in range(1,11):
    if i == snum:
        print(i)
        found=True
        break
if found == False:
    print("Didn't find the secret number!")
