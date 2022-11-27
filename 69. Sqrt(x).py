from math import sqrt



def mySqrt(x: int) -> int:
    return int(sqrt(x))



def mySqrt1(x:int) -> int:
    return int(x**0.5)



def mySqrt3(self, x: int) -> int:
    i = 0
    while True:
        square = i * i

        if square > x:
            return i - 1
        else:
            i += 1

x = 9

print(mySqrt(x))
print(mySqrt1(x))
