# author: Khakhu Ria
# version: 08/12/2024

# find the diffence between the sum of the squares of the 1st 100 natural numbers and the square of their sum
# note that (a+b)^2 > a^2+b^2 for all real numbers a,b

def find_difference(n):
    """
        use the general formula for the sum of squares and the arithmetic sum formula to find the difference between 
        the sum of numbers from 1 to n, all, squared and the sum of squares from 1 to n
    """
    squares_sum = n*(n+1)*(2*n+1)//6
    sum_squared = (n*(n+1)//2)**2
    return sum_squared-squares_sum

if __name__ == "__main__":
    print(find_difference(100))