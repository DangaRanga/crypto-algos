if __name__ == "__main__":
    e = int(input("Enter e: "))
    n = int(input("Enter n: "))
    setqp = False
    for i in range(1,n):
        for j in range(1,n):
            if i * j == n:
                q, p = i , j
                setqp = True
        if setqp:
            break
    et = (q-1) * (p-1)
    for i in range(1, 101):
        if (i * et + 1) % e == 0:
            k = i
            break
    d = int((k * et + 1) / e)
    print("Private Key: ({},{})\n".format(d, n))
    print("Public Key: ({},{})\n".format(e, n))
    print("Factors of N: q = {} , p = {}\n".format(q, p))
    print("Euler's totient: {}\n".format(et))
