import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if y == 1:
        print('B' * x)
        return
    if x == 1:
        for _ in range(y):
            print('B')
        return

    for row in range(y):
        if row == 0 or row == y - 1:
            print('A' + 'B' * (x - 2) + 'C')
        else:
            print('B' + ' ' * (x - 2) + 'B')
