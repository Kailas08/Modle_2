numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = []
for i in numbers[1:]:
    for j in numbers[1:]:
        if (i % j == 0):
            is_prime.append(i)
for i in is_prime:
    if is_prime.count(i) == 1:
        primes.append(i)
    else:
        not_primes.append(i)
not_primes = list(set(not_primes))
print("numbers ", numbers)
print("primes ", primes)
print("not_primes ", not_primes)
