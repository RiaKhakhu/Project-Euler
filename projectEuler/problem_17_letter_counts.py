# author: Khakhu Ria
# version: 14/12/2024

# problem statement: count the number of letters used when the numbers 1 to 1000 are written in words

def count_letters(n):
    """
    count the number of letters used when the numbers from 1 to n are written in words, however n
    is limited to 1000, so far, I am too lazy to generalize this one
    """

    count = 0
    if n > 1000 or n <= 0:
        return "sorry mate, can't do that yet"

    for i in range(1, n + 1):
        num_string = in_words(i)
        for char in num_string:
            if char.isalpha():
                count += 1

    return count


def in_words(n):
    """
    return the word version of a whole number less than or equal to 1000
    """

    def generate_tens(k):
        """
        word representations of integers k where 9<k<100
        """

        if k % 10 == 0:
            return tens[k // 10]
        elif k < 20:
            return tens_2[k]
        else:
            return f"{tens[k // 10]} {units[k % 10]}"

    units = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
             9: "nine"}
    tens = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
            9: "ninety"}
    tens_2 = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
              18: "eighteen", 19: "nineteen"}

    if 0 <= n < 10:
        return units[n]
    elif 10 <= n < 100:
        return generate_tens(n)
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return f"{units[n // 100]} hundred"
        if n % 100 < 10:
            return f"{units[n // 100]} hundred and {units[n % 10]}"
        return f"{units[n // 100]} hundred and {generate_tens(n % 100)}"
    elif n == 1000:
        return "one thousand"
    else:
        return "sorry mate, can't do that one yet"


if __name__ == "__main__":
    print(count_letters(1000))
