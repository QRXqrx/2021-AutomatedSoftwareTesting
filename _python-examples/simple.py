def test(a: int, b: int):
    c = int(a / (b + a - 2))
    if c > 0:
        print(">0")
    else:
        print("<=0")


# Test Driver
if __name__ == '__main__':
    test(0, 0)
