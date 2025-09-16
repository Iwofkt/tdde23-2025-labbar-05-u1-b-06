from numpy._core.strings import isupper
from numpy._core.strings import islower

#A recursive way of splitting a string into one piece
#Containing lowercase, underscores and dots
#and another piece containing uppercase, spaces and pipes.
def split_rec(string: str, split1 = "", split2 = "") -> tuple[str,str]:

    current = string[0]

    if isupper(current) or current == " " or current == "|":
        split1 = str(split1 + current)

    elif islower(current) or current == "_" or current == ".":
        split2 = str(split2 + current)

    if len(string)-1 <= 0:
        return split1, split2
    return split_rec(string[1-len(string):], split1, split2)

#A iterative way of splitting a string into one piece
#Containing lowercase, underscores and dots
#and another piece containing uppercase, spaces and pipes.
def split_it(string):
    split1 = ""
    split2 = ""
    for i in string:
        if isupper(i) or i == " " or i == "|":
            split1 = str(split1 + i)

        elif islower(i) or i == "_" or i == ".":
            split2 = str(split2 + i)
    return split1, split2


print(split_rec("HELLO. Ilove_"))
print(split_it("HELLO. Ilove_"))