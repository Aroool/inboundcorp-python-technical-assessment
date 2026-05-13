import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        if row == 0 or row == y - 1:
            if x == 1:
                print('o')
            else:
                print('o' + '-' * (x - 2) + 'o')
        else:
            if x == 1:
                print('|')
            else:
                print('|' + ' ' * (x - 2) + '|')
