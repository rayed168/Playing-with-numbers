num = int(input("Enter a number : "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    num = num // 10
    reverse = reverse * 10 + remainder
print(reverse)
if temp == reverse:
    print("It is a palindrome number")
else:
    print("It is not a palindrome")
