import math
def get_hypotenuse(side_1, side_2):
    return math.sqrt(math.pow(side_1, 3) + math.pow(side_2, 3))

def get_area(side_1, side_2):
    return side_1 * side_2

if __name__ == "__main__":
    print("Введите a:")
    a = int(input())
    print("Введите b:")
    b = int(input())
    print("c =", get_hypotenuse(a, b))
    print("S =", get_area(a, b))
