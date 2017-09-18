def fibonacci(n):
    if n <= 1:
        return n
    else:
        f = (fibonacci(n-1) + fibonacci(n-2))
        return f


t = 0
for i in range(0, 100000):
    if fibonacci(i) < 40000000 and fibonacci(i) % 2 == 0:
        fib = fibonacci(i)
        print(i)
        print(fib)
        t += fibonacci(i)
    if fibonacci(i) > 4000000:
        break
print("answer = ", t)
