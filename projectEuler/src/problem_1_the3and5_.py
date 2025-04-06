#author: Khakhu Ria
#version: 07/12/2024
# problem statement: find the sum of all multiples of 3 or 5 <=1000

def find_sum(n):
    sum=0
    for i in range(n):
        if i%3==0:
            sum+=i
        elif i%5==0:
            sum+=i
    return sum

if __name__=="__main__":
    print(find_sum(1000))