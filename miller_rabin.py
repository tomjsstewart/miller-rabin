from random import randint

def miller_rabin(n, k):
    n_1 = n - 1
    r = 0
    while n_1 % 2 == 0:
        r += 1
        n_1 //= 2
    d = n_1

    for _ in range(k): # witness loop
        contWit = False
        a = randint(2, n-2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(r-1):
            x = pow(x, 2, n)
            if x == n-1:
                contWit = True
                break
        if contWit: continue
        else:
            return False
    return True
