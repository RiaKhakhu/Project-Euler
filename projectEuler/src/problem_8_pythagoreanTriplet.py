
# author: Khakhu Ria
# version: 10/12/2024

# problem statement: find the only pythagorean triple (a,b,c) where a+b+c = 1000

def find_triple(num):
    """
    Finds a pythagorean triple (a,b,c) such that a+b+c = num
    The algorithm uses Euclid's primitive pythagorean triple generation formula and
    a property of numbers that are part of a primitive pythagorean triple.
    See the page: https://en.wikipedia.org/wiki/Pythagorean_triple for all the theory, and
    most importantly the first special case under the heading "Elementary properties of primitive Pythagorean triples"
    with which this algorithm heavily relies on.
    """
    for i in range(3, num):  # 1 and 2 are not part of any pythagorean triple
        if i % 4 != 2:
            if i % 4 == 0:
                m, n = i // 2, 1
                a, b, c = generate_triple(m, n)
                if a>0 and b>0:
                    if (num / (a + b + c)) - (num // (a + b + c)) == 0:  # check if num/(a+b+c) is an integer
                        k =num // (a + b + c)
                        return k * a, k * b, k * c
            else:
                m, n = (i - 1) // 2 + 1, (i - 1) // 2
                a, b, c = generate_triple(m, n)
                if a > 0 and b > 0:
                    if (num / (a + b + c)) - (num // (a + b + c)) == 0:
                        k = num // (a + b + c)
                        return k * a, k * b, k * c
    return "None found"

def generate_triple(m, n):
    """
    Euclid's primitive pythagorean triple generation formula
    """
    if m<n:
        m,n = n,m
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return a, b, c


if __name__ == "__main__":
    print(find_triple(1000))
