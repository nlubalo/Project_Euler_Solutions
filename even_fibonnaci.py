def fib(n):
    if n==0:
        return 0

    value1, value2 = 1,1
    while n>2:
        value1, value2= value2, value1+value2
        n +=-1

    return value2




def Even_Fib(endNumber):
    n = 0
    sum=0
    cur = fib(n)
    while cur <= endNumber:
        if cur%2==0:
            sum+=cur
        n += 1
        cur = fib(n)
    return sum

print(Even_Fib(4000000))

