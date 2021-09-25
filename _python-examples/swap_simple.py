def test(x: int, y: int):
    z = x - y
    if x > y > 0:
        if z > 0:
            print("z>0")
        else:
            print("z<=0")


# Test Driver
if __name__ == '__main__':
    test(1, 2)
