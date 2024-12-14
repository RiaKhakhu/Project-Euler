# author: Khakhu Ria
# version: 14/12/2024

# problem statement: find the sum of the digits of 2^1000

"""
def find_digit_sum(n):

    if n < 0:
        n = 0 - n

    n = str(n)
    digit_sum = 0

    for digit in n:
        digit_sum += int(digit)

    return digit_sum"""


def find_digit_sum(n):
    """
    given an integer n, find the sum of its digits
    """
    if n < 0:
        n = 0 - n

    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n = n // 10

    return digit_sum


if __name__ == "__main__":
    print(find_digit_sum(2 ** 1000))
