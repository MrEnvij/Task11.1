N = int(input("N = "))

if N >= 1:
    S1 = 1
    if N >= 2:
        S2 = -1

        for n in range(3, N + 1):
            S3 = S2 + n
            print(f"{n} = {S3}")