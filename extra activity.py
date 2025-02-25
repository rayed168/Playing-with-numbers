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

if temp % 2 == 0 and reverse % 2 == 0:
    print("good")
else:
    print("bad")


if temp % 2 != 0 and reverse % 2 != 0:
    print("good")
else:
    print("bad")
