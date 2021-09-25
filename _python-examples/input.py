class Input:

    i64 = 0

    def __init__(self, i: int):
        if i > 10:
            print("\n-------- In <Init>(int)! i > 10")
        else:
            print("\n-------- In <Init>(int! i <= 10")
        self.i64 = 64

    def foo(self, i: int) -> int:
        print("\n-------- In foo! Parameter = ", i)

        assert self.i64 > 0
        if i > self.i64:
            print("i > 64")
            if 5 * i <= 325:
                print("5 * i <= 325")
                if i != 65:
                    print("i != 65")
                else:
                    print("i == 65")
                return i + 3
            elif i != 66:
                print("5 * i > 325 && i != 66")
                return i + 5
            else:
                print("5 * i > 325 && i == 66")
                if True:
                    raise AssertionError("foo failed!")
        elif (i & 7) == 7:
            print("i & 5 == 5")
        print("i <= 64")
        self.i64 = i
        return i


def zoo_sub(j, f):
    if f + j > 256:
        print("i > 73 && f + j > 256")
        return j
    print("i > 73 && f + j <= 256")
    assert False
    return 0


def zoo(i, j, f):
    print("\n-------- In zoo! Parameters = " + i + ", " + j + ", " + f)

    if i > 73:
        zoo_sub(j, f)
    else:
        if i == 12:
            print("i = 12")
        elif i == 42:
            print("i = 42")
        else:
            print("i <= 73")
    return j


# Test Driver
if __name__ == '__main__':
    print("-------- In main!")
    inst = Input(64)
    try:
        inst.foo(-1024)
    except AssertionError:
        print("Assertion Error")
    zoo(1, 2, 1.414)
