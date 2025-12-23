def area(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Rectangle sides must be positive")
    return a * b

def perimeter(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Rectangle sides must be positive")
    return 2 * (a + b)
