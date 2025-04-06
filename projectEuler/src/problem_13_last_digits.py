# author: Khakhu Ria
# version: 13/12/2024

# problem statement: find the last 10 digits of the sum of 50 given 50-digit positive integers( i made this one up)

def find_last_digits_of_sum(n, nums):
    """
    finds the last n digits of the sum of the positive integers in the nums array. Uses the number
    addition algorithm of aligning the numbers and adding column digits from right to left. Here, the
    numbers in the nums array are truncated every iteration.
    """

    if n <= 0:
        return None
    digits = []
    carry_over = 0

    while len(digits) < n:
        col_sum, zeros = 0, 0  # the zeros is to keep track of how many zeros there now is in the nums array

        for i in range(len(nums)):
            col_sum += nums[i] % 10
            nums[i] = nums[i] // 10

            if nums[i] == 0:
                zeros += 1

        col_sum += carry_over
        if zeros == len(nums):  # all columns have been added
            while len(digits) < n:
                if col_sum > 0:
                    digits.append(str(col_sum % 10))
                    col_sum = col_sum // 10
                else:
                    return "Added all numbers and target digits were not reached: " + "".join(digits[::-1])

        else:
            digits.append(str(col_sum % 10))
            carry_over = col_sum // 10

    return "Target digits reached: " + "".join(digits[::-1])


if __name__ == "__main__":
    nums_file = "problem_13_numbers.txt"
    nums = []
    with open(nums_file) as file:
        for line in file:
            nums.append(int(line))

    print(find_last_digits_of_sum(10, nums))
