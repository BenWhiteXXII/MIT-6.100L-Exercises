N = int(input('Enter a positive integer: '))
guess = 1

while guess**3 < N:
    guess += 1
if guess **3 == N:
    print(guess)
else:
    print('Error')
