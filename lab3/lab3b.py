"""Code for n!/(k!(n-k)!) but with minimized calculations starting at choose"""

def faculty_top(q: int, bottom: int) -> int:
    """
    Recursive function that multiplies from q down to bottom + 1
    n * n-1 * n-2 * ... * bottom+2 * bottom+1
    """
    #Base case 1
    if q <= 1:
        return 1
    #Base case 2
    elif q <= bottom + 1:
        return bottom + 1
    return q * faculty_top(q - 1, bottom)

def choose(n: int, k: int):
    if n < k:
        return "n has to be equal to or bigger than k"
    elif n == k:
        return 1
    elif k > (n - k):
        answer = faculty_top(n, k) // faculty_top(n - k, 1)
        return answer

    answer = faculty_top(n, (n - k)) // faculty_top(k, 1)
    return answer
