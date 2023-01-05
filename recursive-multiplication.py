def recursive_multiplication(a, b):
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a
    return a + recursive_multiplication(a, b - 1)

if __name__ == '__main__':
    print(recursive_multiplication(3, 4))
    print(recursive_multiplication(2, 5))
    print(recursive_multiplication(0, 5))
    print(recursive_multiplication(5, 0))
    