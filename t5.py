N = int(input("N = "))
if N == 1:
    xk = 0
elif N == 2:
    xk = 0.5
else:
    a = 0
    b = 0.5
    for k in range(3, N+1):
        xk = b + (((-1)**k) * (k-1))/k
        a, b = b, xk
print(f"{N} = {xk}")