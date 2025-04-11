x = float(input("x = "))
N = int(input("N = "))

xk = 1

for k in range(1, N + 1):
    xk *= (k + 1) * x / (k * k)
    print(f"{k} = {xk}")