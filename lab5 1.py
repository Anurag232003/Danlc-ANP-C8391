def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    primes = []
    
    while count < n:
        if is_prime(num):
            primes.append(num)
            count += 1
        num += 1

    for prime in primes:
        print(prime)

# Number of prime numbers to print
n = 10
print(f"The first {n} prime numbers are:")
print_first_n_primes(n)
