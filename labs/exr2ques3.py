year = int(input("Please enter a year: "))

if year%4 == 0 and (year%400 == 0 and year%100 != 0 ):
    print("Leap Year")
else:
    print("Not a Leap Year")