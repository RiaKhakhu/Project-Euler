# author: Khakhu Ria
# version: 14/12/2024

# problem statement: find the starting number in the collatz sequence under 1,000,000; that takes the longest
# steps to converge to 1

def find_longest_chain(n):
    """
    return the starting number x in the collatz sequence that takes the longest steps to converge to 1, where 1<x<n, and
    n>=2
    """
    nums, max_steps = [], 0
    for starting_number in range(2, n):
        x = starting_number
        steps = 0
        while x > 1:
            if x % 2 == 0:
                x = x // 2

            else:
                x = 3 * x + 1

            steps += 1
        if steps > max_steps:
            nums, max_steps = [starting_number], steps

        elif steps == max_steps:
            nums.append(starting_number)

    if len(nums) > 1:
        return f"The starting numbers: {nums}, converged in {max_steps} steps."
    elif len(nums) == 1:
        return f"The starting number: {nums[0]}, converged in {max_steps} steps."
    else:
        return "Input must be greater than 2."


if __name__ == "__main__":
    print(find_longest_chain(1000000))
