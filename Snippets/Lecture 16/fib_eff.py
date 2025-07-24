def fib_eff(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_eff(n-1, d) + fib_eff(n-2, d)
        d[n] = ans
        return ans

d= {1:1, 2:1}
print(fib_eff(6, d))
