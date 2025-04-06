# author: Khakhu Ria
# version: 12/12/2024

# problem statement: find the sum of all primes below 2,000,000
# The solution to this is almost identical to the solution to problem 7

def find_primes_sum(n):
    """
    Using a slightly modified Sieve of Eratosthenes, this function sums all primes below n (inclusive)

    """
    compositeNumbers = {}  # dictionary of necessary composite numbers, to help identify primes, key(composite number): value(one of its prime factors)
    primes_sum = 0
    for i in range(2, n + 1):
        if i in compositeNumbers:
            primeFactor = compositeNumbers[i]
            next_multiple = i + primeFactor

            # avoid complications where 2 prime factors have the same composite-number-key
            while next_multiple in compositeNumbers:
                next_multiple += primeFactor

            compositeNumbers[next_multiple] = primeFactor
            del compositeNumbers[i]  # remove unnessesary composite numbers to free up memory
        else:
            compositeNumbers[i * i] = i
            primes_sum += i

    return primes_sum


if __name__ == "__main__":
    print(find_primes_sum(2000000))
