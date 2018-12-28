def Multiples_3_and_5(start, stop):
    sum =0
    for i in range(start, stop):
        if i%5==0 or i%3==0:
            sum+=i
    
    return sum

print(Multiples_3_and_5(1,1000))


