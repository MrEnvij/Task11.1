def gen_1(x, N):
    xk = x
    for k in range(1, N + 1):
        xk *= x * x / (2 * k * (2 * k + 1))
        yield k, xk

def gen_2(x, N):
    if N >= 1:
        xk = -x
        for k in range(2, N + 1):
            xk *= -x * (k - 1) / k
            yield k, xk

def gen_3(x, N):
    xk = 1
    for k in range(1, N + 1):
        xk *= (k + 1) * x / (k * k)
        yield k, xk

def gen_4(N):
    if N >= 1:
        S1 = 1
    if N >= 2:
        S2 = -1
    if N >= 3:
        for n in range(3, N + 1):
            S3 = S2 + n
            S1, S2 = S2, S3
            yield n, S3

def gen_5(N):
    if N == 1:
        yield 1, 0
    elif N == 2:
        yield 2, 0.5
    else:
        a = 0
        b = 0.5
        for k in range(3, N + 1):
            xk = b + ((-1) ** k) * (k - 1) / k
            a, b = b, xk
            yield k, xk

def infinite_gen(start=1):
    k = start
    while True:
        yield k, k ** 2
        k += 1

def main():
    print("Генератор 1:")
    for k, val in gen_1(x=2.0, N=5):
        print(f"{k} = {val}")

    print("\nГенератор 2:")
    for k, val in gen_2(x=1.5, N=5):
        print(f"{k} = {val}")

    print("\nГенератор 3:")
    for k, val in gen_3(x=1.0, N=5):
        print(f"{k} = {val}")

    print("\nГенератор 4:")
    for k, val in gen_4(N=7):
        print(f"{k} = {val}")

    print("\nГенератор 5:")
    for k, val in gen_5(N=6):
        print(f"{k} = {val}")

    print("\nНескінченний генератор:")
    gen = infinite_gen()
    for _ in range(5):
        k, val = next(gen)
        print(f"{k} = {val}")

if __name__ == "__main__":
    main()
