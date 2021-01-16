num=int(input("enter a number:"))
rev=0
temp=num
dig=0
while temp:
    dig=temp%10
    rev=(rev*10)+dig
    temp=temp//10
if num==rev:
    print("palindrome")
else:
    print("not palindrome")
