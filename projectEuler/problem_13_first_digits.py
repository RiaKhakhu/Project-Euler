# author: Khakhu Ria
# version: 14/12/2024

# problem statement: find the first 10 digits of the sum of 50 50-digit positive integers

def find_first_digits(n, num):
    """
    given a number called num, find its first n digits
    """

    num = str(num)
    if len(num) < n:
        return f"Number is shorter than digits specified: {num}"

    else:
        return f"First {n} digits are: {num[:n]}"


def find_sum(nums):
    """
    given an array of numbers, return their sum
    """
    nums_sum = 0

    for num in nums:
        nums_sum += num

    return nums_sum


if __name__ == "__main__":
    nums_file = "problem_13_numbers.txt"
    nums = []
    with open(nums_file) as file:
        for line in file:
            nums.append(int(line))

    nums_sum = find_sum(nums)
    print(find_first_digits(10, nums_sum))
