# author: Khakhu Ria
# version: 13/12/2024

# problem statement: given a 20 x 20 matrix of positive integers, find the largest product of 4 adjacent numbers.
# which may be horizontally, vertically or diagonally adjacent

def find_max_product(k, matrix):
    """
    Given an m by n matrix of integers, this function finds the largest product of k adjacent numbers ( horizontal,vertical or diagonal)
    """
    width = len(matrix[0])
    height =0
    for row in matrix:
        height+=1

    max_horizontal = find_max_horizontal(k,matrix,width)
    max_vertical = find_max_vertical(k, matrix, height, width)
    max_right_diagonal = find_max_right_diagonal(k, matrix,height, width)
    max_left_diagonal = find_max_left_diagonal(k, matrix,height, width)

    return max(max_horizontal[0], max_vertical[0], max_right_diagonal[0],max_left_diagonal[0])

def find_max_horizontal(k,matrix,width):
    """
    find the max product of k horizontally adjacent numbers in a rectangular matrix of width "width"
    """
    max_product, max_product_nums = 0, [0]
    for row in matrix:
        for col in range(width-k+1):
            nums = row[col:col+k]
            product = find_product(nums)
            if product>max_product:
                max_product, max_product_nums = product, nums

    return max_product, max_product_nums


def find_max_vertical(k,matrix,height,width):
    """
    find the max product of k vertically adjacent numbers in a height by width rectangular matrix
    """
    max_product, max_product_nums = 0, [0]

    for row in range(height-k+1):
        for col in range(width):
            nums = [matrix[row+i][col] for i in range(k)]
            product = find_product(nums)
            if product > max_product:
                max_product, max_product_nums = product, nums

    return max_product, max_product_nums


def find_max_right_diagonal(k,matrix,height,width):
    """
    find the max product of k diagonally adjacent numbers. note that the right diagonal is the positive-slope diagonal
    in any k by k matrix
    """
    max_product, max_product_nums = 0, [0]

    for row in range(k-1,height):
        for col in range(width-k+1):
            nums = [matrix[row-i][col+i] for i in range(k)]
            product = find_product(nums)
            if product>max_product:
                max_product, max_product_nums = product, nums

    return max_product, max_product_nums


def find_max_left_diagonal(k,matrix,height,width):
    """
    find the max product of k diagonally adjacent numbers. note that the left diagonal is the negative-slope diagonal
    in any k by k matrix
    """
    max_product, max_product_nums = 0, [0]

    for row in range(height-k+1):
        for col in range(width-k+1):
            nums = [matrix[row+i][col+i] for i in range(k)]
            product = find_product(nums)
            if product>max_product:
                max_product, max_product_nums = product, nums

    return max_product, max_product_nums


def find_product(nums):
    """
    find the product of the integers in the given nums array
    """
    if not nums:
        return "Empty list"

    product = 1
    for num in nums:
        product*=int(num)

    return product

if __name__ == "__main__":
    matrix_file = "problem_11_20x20_matrix.txt"
    num_matrix = []
    with open(matrix_file) as file:
        for line in file:
            row = line.split()
            num_matrix.append(row)

    print(find_max_product(4,num_matrix))