print("WELCOME TO PYTHON PIZZA DELIVERY!!")
size=input("What type of size do you want?type s,m,l:")
pepperoni=input("Do you want pepperoni on your pizza? y or n:")
extra_cheese=input("Do you want extra cheese on your pizza? y or n:")
#USING ELIF(SIZE)
if size=="s":
    bill=15
elif size=="m":
    bill=20
elif size=="l":
    bill=25
else:
    print("you typed the wrong input") 
#USING NESTED IF(PEPPERONI)
if pepperoni=="y":
    if size=="s":
        bill +=2
    else:
        bill +=3    
#(EXTRA CHEESE)
if extra_cheese=="y":
    bill +=1

#FINAL BILL
print(f"Your final bill is ${bill}")


    
        
    


