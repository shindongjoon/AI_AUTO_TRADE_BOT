from my_package.sum import sum_ab, Calculator, print_name
from my_package.sub import sub_ab


if __name__ == '__main__':
    x2 = sum_ab(3,4)
    y2 = sub_ab(4,1)
    print(f"x2 : {x2}, y2 : {y2}")

    c = Calculator(1, 2)
    print(f"c.sum() : {c.sum()}")
    print_name()