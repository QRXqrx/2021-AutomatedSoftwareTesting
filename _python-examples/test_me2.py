def test_me2(x: int, b: bool):
    print("!!!!!!!!!!!!!!! First step! ")

    if b:
        if x <= 5:
            print("  <= 5")
        if x >= 7:
            print("  <= 7")


# Test Driver
if __name__ == '__main__':
    print("!!!!!!!!!!!!!!! Start Testing! ")
    test_me2(42, True)
