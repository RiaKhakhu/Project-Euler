# author: Khakhu Ria
# version: 13/12/2024

from math import sqrt


# problem statement: find the first triangular number with 500 divisors

def first_triangular_n_divisor(n):
    """
    finds the first triangular number with at least n divisors
    """
    k = 1

    while True:
        triangular_number = k * (k + 1) // 2

        if number_of_divisors(triangular_number) >= n:
            return triangular_number

        k += 1


def number_of_divisors(n):
    """
    finds the number of divisors of an integer n
    """
    if n < 0:
        n = 0 - n

    if n == 1:
        return 1

    prime_signature = {}
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i in prime_signature:
                prime_signature[i] += 1

            else:
                prime_signature[i] = 1

            n = n // i

        else:
            i += 1

    if n in prime_signature:
        prime_signature[n] += 1
    else:
        prime_signature[n] = 1

    num_of_divisors = 1
    for prime in prime_signature:
        num_of_divisors *= (prime_signature[prime] + 1)

    return num_of_divisors


if __name__ == "__main__":
    print(first_triangular_n_divisor(500))
