#Find the control number in personal identity numbers

#the main function
def check_pnr(pnr):
    print(f"checking personal control number for {pnr}")
    #Get product of pnr without the control number
    prod = multi_weight(pnr[:-1])
    #Check digit sum
    total=digit_sum(prod)
    #check difference to the closest tens up giving us the control number
    control_number = dif_to_ten(total)
    #check validity
    result = check_valid(pnr[-1],control_number)
    return result


#Multiply first numb with 2, second with 1, third with 2...
def multi_weight(pnr):
    multi = 2
    for i in range(len(pnr)):
        if multi == 2:
            pnr[i] *= multi
            multi = 1
        else:
            multi = 2
    return pnr


#Digit sum of an array
def digit_sum(arr):
    def digit_sum(n):
        #Sum of all digits for all d in a number
        return sum(int(j) for j in str(n))
    #Sum of all numbers in the array
    return sum(digit_sum(i) for i in arr)


#Dif between number and closest tens up
def dif_to_ten(total):
    #Check nearest tens down
    control_number = (total // 10) * 10
    #If differance is 0 return differance
    if control_number == total:
        return 0
    #check difference with nearest tens up
    return control_number + 10 - total


#Check if last number in array is equal to other given number
def check_valid(pnr, control_number):
    print(f"{pnr} {control_number}")
    return pnr == control_number


