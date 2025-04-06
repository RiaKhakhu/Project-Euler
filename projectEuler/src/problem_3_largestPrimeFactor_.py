# author: Khakhu Ria
# version: 07/12/2024
# problem statement :find the largest prime factor of 600851475143

#assuming n>1
def largestPrimeFactor(n):
    """
        return largest prime factor of n, where n is a positive integer >1. Works by removing all prime factors from n starting from 2,
        until only 1 prime factor remains, which is the largest. This is an application of Trial division,
        see wikipedia page: https://en.wikipedia.org/wiki/Trial_division
    """
    if n<2:
        return "Must be a positive integer >1"
    i = 2
    while i*i <= n:
        if n%i==0:
            n=n//i
        else:
            i+=1
    return n


    
if __name__=="__main__":
    print(largestPrimeFactor(600851475143))