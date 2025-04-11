x = float(input("x = "))
N = int(input("N = "))
xk = x

for k in range(1, N + 1):
    xk *= x * x / (2 * k * (2 * k + 1))
    print(f"{k} = {xk}")