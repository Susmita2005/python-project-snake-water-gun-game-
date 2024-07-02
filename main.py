

import random
'''

1 for snake
-1 for water
0 for gun

'''


computer=random.choice([1,-1,0])
youstr=input("Enter your choice  :")
youdict={"s" :1 ,"w" :-1, "g":0}
reversedict={1 :"Snake",-1:"water",0:"gun"}



you=youdict[youstr]

print(f"you choose {reversedict[you]} and computer choose {reversedict[computer]}")

if (computer==you):
    print("It's draw")
else:
    if(computer==1 and you==-1):
        print("You lose")
    elif(computer==1 and you==0):
        print("You win")
    elif(computer==-1 and you==1):
        print("You win")
    elif(computer==-1 and you==0):
        print("You lose")
    elif(computer==0 and you==1):
        print("You lose")
    elif(computer==0 and you==-1):
        print("You win")
    else:
        print("something went wrong")

    


