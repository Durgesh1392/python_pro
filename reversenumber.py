def reverse(x):
    negative = False
    if x < 0:
        negative = True
        x = -1 * x

    rev = 0
    while x > 0:
        rev = rev * 10 + (x % 10)
        x //= 10

    if rev > (2 ** 31 - 1) or rev < (-2 ** 31):
        return 0

    if negative:
        return -1 * rev
    else:

        return rev


if __name__ == '__main__':

     print(reverse(1234))
