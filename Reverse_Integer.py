def reverse(x):

    # Converting the integer into list of digits
    digits = [int(num) for num in str(x)]

    # Reversing the digits
    temp = 0
    for n in range(len(digits) - 1):
        temp = digits[n]
        digits[n] = digits[len(digits) - 1 - n]
        digits[len(digits) - 1 - n] = temp

    # Reconverting the list to an integer
    s = [str(digit) for digit in digits]
    i = int("".join(s))

    return i


print(reverse(12345))
# 0, 1, 2, 3, 4
