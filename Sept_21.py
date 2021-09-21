import random

pd1 = ["Alejandro Alonso", "Yusuf Elsharawy", "Deven Maheshwari"]
pd2 = ["Fake Name1", "Fake Name2", "Fake Name3"]

def writeName():
    period = random.randint(0,1)
    if (period):
        index = random.randint(0,len(pd1)-1)
        print(pd1[index])
    else:
        index = random.randint(0, len(pd2)-1)
        print(pd2[index])
    
writeName()
