#author: Khakhu Ria
#version: 09/12/2024

#problem statement: find the largest palindrome which is a product of 2 3-digit positive integers
# i feel this can be greatly optimized

def find_largest_palindrome(n):
    """
    using a brute force approach, we check all permutations for the product of 2 n-digit numbers and return the largest prime found,
    and the pair of numbers that made the product
    
    """
    start= 10**(n-1) 
    stop = 10**(n)
    largestPalindrome, product_pair = 0, (0,0)
    for i in range(start,stop):
        for j in range(start, stop):
            product= i*j
            if isPalindrome(product) and product > largestPalindrome:
                largestPalindrome = product
                product_pair = (i,j)
    return [largestPalindrome,product_pair]

def isPalindrome(n):
    """
        check if n is a palindrome
    """
    n = str(n)
    for i in range(len(n)//2):
        if n[i]!=n[-1-i]:
            return False
        
    return True


if __name__=="__main__":
    print(find_largest_palindrome(3))