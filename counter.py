# WAP to print numbers from 60 to 0 using recursion for traffic signal.
def counter(n):
    if n <= 0:
        print("stop")
    else:
        print(n)
        counter(n-1)
    
counter(60)
