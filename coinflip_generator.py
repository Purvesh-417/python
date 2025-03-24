import random
print("welcome to coin flip generator")
input("press enter to flip a coin")
random_heads_or_tails=random.randint(0,1)

if random_heads_or_tails==0:
     print("head")
else:     
    print("tails")