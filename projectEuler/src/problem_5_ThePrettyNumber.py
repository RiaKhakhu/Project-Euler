#author: Khakhu Ria
#version: 07/12/2024

# problem statement: find smallest number evenly divisible by all numbers from 1 to 20, i.e the lcm of the numbers 1 to 20

def gcd(a,b):
    """
       use euclids algorithm to find the greatest common divisor of 2 positive integers
    """
    if a < b:
        a,b = b,a
    while b>0:
        remainder = a%b
        a,b = b,remainder
    return a
    
def findlcm(nums):
    """
    find the lcm of all the numbers in the given list
    
    """
    if not list:
        return "do you think im dumb bro?"

    else:
        lcm = nums[0]
        for i in range(1,len(nums)):
            lcm = (lcm*nums[i])//gcd(lcm,nums[i]) # using the fact that lcm(a,b) = a*b/gcd(a,b)
    return lcm


if __name__ == "__main__":
    print(findlcm([i for i in range(1,20)]))



