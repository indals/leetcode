def generator_fibonacci_series():
    n3=1
    n2=1
    while True:
        n1=n2
        n2=n3
        n3=n1+n2
        yield n1

fibo_generator=generator_fibonacci_series()
for i in range(100):
    print(next(fibo_generator))