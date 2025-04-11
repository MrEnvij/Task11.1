x = float(input("x = "))
N = int(input("k_max = "))

if N >= 1:
    xk = -x

    for k in range(2, N + 1):
        xk *= -x * (k - 1) / k
        print(f"{k} = {xk}")
