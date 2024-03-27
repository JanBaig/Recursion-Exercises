
def fib(N):
    if N < 2: return N
    return fib(N - 1) + fib(N - 2)

if __name__ == "__main__":
    print(fib(6)) 

# Remember: fib(num-1) and fib(num-2) don't get called together, the right only gets executed after the completion of the left
# This is non tail recursive