
# author: Khakhu Ria
# version: 10/12/2024

# problem statement: find the only pythagorean triple (a,b,c) where a+b+c = 1000

"""
     The below solution is based on first doing some algebraic manipulations
     Key fact discovered: ab is a multiple of 1000, so below i let ab = 1000k for some
     natural number k
     After some math, a = ((500+k)+or-sqrt((500+k)^2-4000k))/2 , using this i will find the value
     of b and c again using some elementary algebra

"""


def find_triple(n):
    """
    Find a pythagorean triple (a,b,c) such that a+b+c = n
    The algorithm uses Euclid's primitive pythagorean triple generation formula and
    a property of numbers that are part of a pythagorean triple.
    See the page: https://en.wikipedia.org/wiki/Pythagorean_triple for all the theory,
    most importantly the first special case under the heading "Elementary properties of primitive Pythagorean triples"
    """
    for i in range(3, n):  # 1 and 2 are not part of any pythagorean triple
        if i % 4 != 2:
            if i % 4 == 0:
                m, n = i // 4, 1
                a, b, c = generate_triple(m, n)
                if a>0 and b>0 and c>0:
                    if (1000 / (a + b + c)) - (1000 // (a + b + c)) == 0:  # check if 1000/(a+b+c) is an integer
                        k = 1000 // (a + b + c)
                        return k * a, k * b, k * c,i
            else:
                m, n = (i - 1) // 2 + 1, (i - 1) // 2
                a, b, c = generate_triple(m, n)
                if a > 0 and b > 0 and c > 0:
                    if (1000 / (a + b + c)) - (1000 // (a + b + c)) == 0:
                        k = 1000 // (a + b + c)
                        return k * a, k * b, k * c,i
    return "None found"

def generate_triple(m, n):
    """
    Euclid's primitive pythagorean triple generation formula
    """
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return a, b, c


if __name__ == "__main__":
    print(find_triple(1000))
