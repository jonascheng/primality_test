import sys
import math


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, round(math.sqrt(n))):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__== "__main__":
    input = int(sys.argv[1])
    ret = is_prime(input)
    if ret == True:
        print(f'{input} is prime')
    else:
        print(f'{input} is not prime')
