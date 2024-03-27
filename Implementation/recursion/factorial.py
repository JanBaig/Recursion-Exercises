
def factorial(N):
    if N == 1: return 1
    return N * factorial(N-1)

def factorialTail(num, result):
    if num == 1: return result
    return factorialTail(num - 1, result * num)

if __name__ == "__main__":
    print(factorialTail(4, 1))

# (4, 1)
# (3, 1 * 4)
# (2, 4 * 3)
# (1, 12 * 2)
# (1) -> 24

# Non Tail recursive: The Answer is dependant on the return value of each and every function call in the stack 
# Tail recursion: The final answer of the function is only dependant on the return value of the last recursive function call
# Great Resource: https://www.programmerinterview.com/recursion/tail-recursion/
