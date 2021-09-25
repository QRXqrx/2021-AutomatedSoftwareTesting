def branch(x: int, y: int):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x < y:
        print("abs(x)<abs(y)")
    elif x == 0:
        print("x==y==0")
    else:
        print("x>=y>=0")


# Test Driver
if __name__ == '__main__':
    branch(1, 2)
