# Guess the cube root of a number using bisection search

cube = 27
epsilon = 0.01
low = 0
high = cube
guess = (high + low) / 2
guess_count = 0

# checks if the guess is within range of the epsilon
while abs(guess**3 - cube) >= epsilon:
    # bisection search
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    # generates new guess based on new high and low pointers
    guess = (high + low) / 2
    print(guess)
    guess_count += 1

print(f'Cube root of {cube} is approx.{guess}')
print(f'Guessed in {guess_count} guesses')
