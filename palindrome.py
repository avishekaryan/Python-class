# WAPP to check wether a number is palindrome or not .

num = int(input("Enter any number of more than 1 digit : "))
temp = num         # temp is variable to store user input no as num will be changed to another value in loop.
rev = 0            # initalize reverse variable to 0

while num > 0 :          # loop will run until num is greater than 0
    rem = num % 10       # remender(rem) will store the last digit of num
    rev = rev * 10 + rem  # rev will store the reverse of num
    num = num // 10  # num will be updated to remove the last digit

if temp == rev :
    print(f'{temp} is a Palindrome number')
else :
    print(f'{temp} is Not a palindrome number')


'''
If we use for loop then we need to count the number of digits in the number first and then use that count to 
reverse the number. But using while loop we can reverse the number without counting the digits.
and other conditions and logic will be same for both loops.
'''
# for i in range(len(str(num))):      in this loop will run until the number of digits in num




# WAPP to check weather a word/string is palindrome or not.
# This can also check for palindrome number. 
value = input("Enter any Value :").lower()

if value == value[::-1] :
    print(f'{value} is a Palindrome')
else :
    print(f'{value} is Not a palindrome')
