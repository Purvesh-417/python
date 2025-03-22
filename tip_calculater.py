print("welcome to the tip calaculater!")
bill=float(input("what was the total bill?:"))
tip=int(input("how much percentage of tip would you like to give? 10,12,15 or 20?:"))
people=int(input("how many people to split up the bill?:"))
x=tip/100
y=x*bill
z=y+bill
total=round(z/people,2)
print(f"each person should pay:{total}")