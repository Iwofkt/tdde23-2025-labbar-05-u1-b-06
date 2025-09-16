#This program finds the biggest number of 2, 3 or more numbers

#returns biggest of 3 values 
def max3(a,b,c): 
    return max2(max2(a,b),c)


#returns biggest of 2 values 
def max2(a,b):
    return max(a,b)

#necesary ends here

#ask user until given a valid number
def ask_num(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("That's not a valid number. Please try again.")


#Find the biggest number in array
def max_any(arr):
    #If array is empty return None
    if not arr:
        return None
    #Find the biggest number in array
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num


#Script starts here
def main():
    #Ask the user for amount of values
    amount_of_num = ask_num("How many numbers do you want to compare?: ")
    num = [0] * amount_of_num
    
    #Ask the user to set all values
    for index in range(amount_of_num):
        num[index] = ask_num(f"What's your number {index + 1}? ")

    print(f"The biggest number is: {max_any(num)}")


if __name__ == "__main__":
    main()