num=int(input("enter a number:"))
rev=0
temp=num
dig=0
while temp:
    dig=temp%10
    rev=(rev*10)+dig
    temp=temp//10
print("reverse of a number:",rev)
