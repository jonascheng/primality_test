import sys
import random


def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # determin test list
    A = range(2, n - 2)
    # determin k
    k = int(len(A) / 2)

    for _ in range(k):
        a = random.choice(A)
        if a ** (n - 1) % n != 1:
            return False

    return True


if __name__== "__main__":
    input = int(sys.argv[1])
    ret = is_prime(input)
    if ret == True:
        print(f'{input} is probably prime')
    else:
        print(f'{input} is not prime')

