#Code for n!/(k!(n-k)!) but with minimized calculations starting at choose

# Recursive function that multiplies from q down to bottom + 1
# n, n-1, n-2... bottom+2, bottom+1
def faculty_top(q: int, bottom: int) -> int:
    # If q is 1 or less, return 1 as base case for multiplication
    if q <= 1:
        return 1

    # If q is at or just above bottom + 1, stop recursion and return bottom + 1
    # This acts like the stopping point in the descending multiplication
    elif q <= bottom + 1:
        return bottom + 1

    # Multiply current q with faculty_top of (q-1) down to bottom
    return q * faculty_top(q - 1, bottom)


# Calculate binomial coefficient n choose k: C(n,k) = n! / (k! (n-k)!)
def choose(n: int, k: int):

    # If k is greater than n, combination is invalid
    if n < k:
        return "n has to be equal to or bigger than k"

    # If k == n, only one way to choose all elements
    elif n == k:
        return False

    # Use symmetry property C(n, k) = C(n, n-k) to minimize calculations
    elif k > (n - k):
        # Numerator: product from n down to k+1
        # Calculate denominator: product from (n-k) down to 1
        answer = str(faculty_top(n, k) // faculty_top(n - k, 1))
        return answer

    #Nnumerator: product from n down to (n-k)+1
    #Denominator: product from k down to 1
    answer = str(faculty_top(n, (n - k)) // faculty_top(k, 1))
    print(answer)
    return answer