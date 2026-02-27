# WAP to print all even numbers from 1 to 50 using a while loop.

n = 1
counter = 0                # this variable is used to count the number of even numbers from 1 to 50.
while n <= 50 :
    if n%2 == 0 :
        print(n, end=" ")  # end=" " is used to print the numbers in the same line with horizontally with a space in between.
        counter += 1       # this is used to increment the counter variable by 1 each time we find an even number.
    n = n + 1        # we can also write n += 1 instead of n = n + 1 .
                           # if we print without end=" " then it will print the numbers vertically in different lines.

print('\nNumber of even numbers between 1 and 50 : ', counter)
