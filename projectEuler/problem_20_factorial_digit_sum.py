# author: Khakhu Ria
# version: 14/12/2024

# problem statement: find the digit sum of 100!

from problem_16_digit_sum import find_digit_sum


def factorial(n):
    """
    return the value of n!, where n is a non-negative integer
    """
    if n == 0 or n == 1:
        return 1

    else:
        product = 1
        for i in range(2, n + 1):
            product *= i

    return product


if __name__ == "__main__":
    print(find_digit_sum(factorial(100)))
