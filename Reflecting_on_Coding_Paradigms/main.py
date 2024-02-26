from typing import List

def convert_2d_arry(array) -> List:
    # Two ways to flatten and sort an array
    result = []
    row = len(array)
    col = len(array[0])
    for r in range(row):
        for c in range(col):
            result.append(array[r][c])
    result.sort()
    return result

def main():
    a = ((1, 2),(2, 7),(4, 5))
    print(convert_2d_arry(a))
    b = ((1, -2, 4),(2, -7, 5),(4, 5, 10))
    print(convert_2d_arry(b))
    c = ((-11, 2),(2, 10),(4, 25))
    print(convert_2d_arry(c))
    

if __name__ == "__main__":
    main()