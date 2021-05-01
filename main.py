import random


def ModularExpo(a, b_r, n):
    d = 1
    temp = b_r
    b = [0] * 100
    k = 0
    c = 0
    while temp > 0:
        b[k] = temp % 2
        temp = temp >> 1
        k = k + 1

    i = k
    while i >= 0:
        c = 2 * c
        d = (d * d) % n
        if b[i] == 1:
            c += 1
            d = (d * a) % n
        i = i - 1
    return d


def witness(a, n):
    x = [0] * 10
    k = 0;
    m = n - 1;
    while m % 2 == 0:
        m = m / 2;
        k = k + 1
    # x[0] = pow(a,int(m),n)
    x[0] = ModularExpo(a, int(m), n)
    i = 1
    while i <= k:
        x[i] = ModularExpo(x[i - 1], 2, n)
        if x[i] == 1 and x[i - 1] != 1 and x[i - 1] != n - 1:
            return True
        i = i + 1
    if x[k] != 1:
        return True
    return False


def MR(n, s):
    for j in range(s):
        a = random.randint(1, n - 1)
        if witness(a, n):
            print(f"{n} is Composite")
            return False
    print(f"{n} is Prime")
    return True


MR(99999985557, 10)
