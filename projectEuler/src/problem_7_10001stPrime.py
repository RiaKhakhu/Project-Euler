# author: Khakhu Ria
# version: 09/12/2024
# problem statement: find the 10001st prime number

def findPrime(n):
    """
    using incremental sieve of eratosthenes to find nth prime
    
    """
    compositeNumbers = {} # dictionary of necessary composite numbers, key(composite number): value(one of its prime factors)

    nth_prime = -1
    discoveredPrimes = 0
    i = 2
    while discoveredPrimes < n:
        if i in compositeNumbers:
            primeFactor = compositeNumbers[i]
            next_multiple = i+primeFactor
            while next_multiple in compositeNumbers: # avoid complications where 2 prime factors have the same composite-number-key
                next_multiple+=primeFactor
            compositeNumbers[next_multiple] = primeFactor
            del compositeNumbers[i] # remove unnessesary composite numbers to free up memory
        else:
            compositeNumbers[i*i]=i
            nth_prime=i
            discoveredPrimes+=1
        i+=1
    return nth_prime


if __name__ == "__main__":
    print(findPrime(10001))

