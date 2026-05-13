# Python Technical Assessment

Character-based terminal graphics in Python. Each assignment implements a `rush(x, y)` function that draws a rectangular pattern of width `x` and height `y`.

## Structure

```
rush-1-1/   # Rectangle using o, -, |
rush-1-2/   # Rectangle using /, \, *
rush-1-3/   # Rectangle using A, B, C (A top corners, C bottom corners)
rush-1-4/   # Rectangle using A, B, C (A left, C right, same top & bottom)
rush-1-5/   # Rectangle using A, B, C (diagonal corners swap on bottom)
```

## Usage

Each assignment is run with the provided `main.py`:

```bash
python main.py x y
```

## Notes

- Prints `Invalid size` to stderr and returns if `x <= 0` or `y <= 0`
- All output is terminal-based using `print()`
