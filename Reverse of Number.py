n = int(input("Enter no.= "))
temp = n
rem=0
rev=0
while temp!=0:
    rem = temp%10
    rev = rev*10 + rem
    temp = temp//10
print("Reverse of ",n," is = ",rev)
