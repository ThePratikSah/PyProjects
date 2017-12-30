def prime(num):
    f = 0
    for i in xrange(2, num - 1):
        if num % i == 0:
            f = 1
            return 0
            break
    if f == 0:
        return 1


for j in xrange(2, 100):
    catch = prime(j)
    if catch == 1:
        print(j)
