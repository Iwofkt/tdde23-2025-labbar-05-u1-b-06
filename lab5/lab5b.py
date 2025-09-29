
import math
def unsharp_mask(dim:int):
    return_list = []
    for y in range(dim):
        for x in range(dim):
            x = x-(dim//2)
            y = y-(dim//2)
            print(x,y)
            if x == 0 and y == 0:
                return_list.append(1.5)
            return_list.append(value(x,y))
    return return_list

def value(x,y):
    s=4.5
    ret = (-1/(2*math.pi*s**2))*math.e**-(((x ** 2) + (y ** 2)) / (2 * s ** 2))
    return ret

print(unsharp_mask(2))