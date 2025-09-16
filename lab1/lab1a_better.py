#A program that asks for a number and then divides it by three and then prints it

#divide by three
def div_by_three(n):
    return n/3

#ask for num and if not valid num try again
def ask_num(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("That's not a valid number. Please try again.")

#Check if n/3 is an integer
def is_int(n):
    if(n%3):
        return("false")
    return("ture")

#Main function that runs first
def main():
    choise = ask_num("What's the number you want to divide by 3?: ")
    answer = div_by_three(choise)
    print(f"{choise} divided by 3 is {answer}")
    print(f"it is {is_int(choise)} that {choise} is an int when divided with 3.")

if __name__ == "__main__":
     main()
