def wilsons_theorem(n):
    """
    * n is a natural number > 1
    Checks if n is a prime number
    """
    if (factorial(n - 1) % n) == -1 % n:
        return True

def factorial(a):
    """
    * a is a number
    produces a! i.e. if a=3 then a!=3*2*1=6
    """
    y = 1
    for x in range(1, a+1):
        y = y*x
    return(y)

def check_range(a):
    """
    * a is an natural number
    finds all primes within the range a using Wilson's theorem
    """
    count = 0
    nums = []
    for i in range(2,a+1):
        if wilsons_theorem(i) == True:
            count += 1
            nums.append(i)
    print(f"There are {count} natural numbers that are prime in the range of {a}")
    print("Here are those numbers:")
    print(nums)

check_range(int(input("Enter range: ")))
