N = int(input('Enter integer: '))
high = 1000
low = 0
count = 0
guess = (high + low) / 2

while guess != N:
    if guess > N:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
    count += 1

print(f'answer: {guess}')
print(f'count: {count}')
