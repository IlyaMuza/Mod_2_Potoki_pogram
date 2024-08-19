#numbers = []
#for l in range(1,10000):
#    numbers.append(l)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
for i in numbers:
    is_prime = False
    k = round(i ** 0.5)
    for j in range(1,k+1):
        if (i % j == 0) and (j != 1) and (i != j):
            is_prime = True
            break
    if is_prime:
        not_primes.append(i)
    else:
        primes.append(i)
print(primes)
print(not_primes)