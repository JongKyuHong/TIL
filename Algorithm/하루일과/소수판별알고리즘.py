import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지 확인한다. 궂이 x까지 확인하지 않아도 된다.
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
