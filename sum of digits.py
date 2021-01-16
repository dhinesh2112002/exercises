num=int(input("enter a number:"))
tot=0
temp=num
dig=0
while temp:
    dig=temp%10
    tot+=dig
    temp=temp//10
print("sum of digits:",tot)
    
    
    
