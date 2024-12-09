# author: Khakhu Ria
# version: 07/12/2024

# problem statement: find the sum of all even fibonacci numbers < 4000000, with the 1st 2 terms: 1,2

def find_even_fibonaccis(n):
    """
       find sum of all even fibonaccis <n
    """
    sum=0
    prev_term,curr_term = 1,2 # 1st 2 terms of fibonacci sequence
    while curr_term<n:
        if (curr_term)%2==0:
            sum+=curr_term
        next_term = prev_term+curr_term   
        prev_term,curr_term = curr_term,next_term
    return sum

if __name__ =="__main__":
    print(find_even_fibonaccis(4000000))

