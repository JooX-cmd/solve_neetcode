#frist loop every time  
    #IF  user  en y 
import random
while True:
    choice = str(input("roll the dice? (y /n):  ")).lower()
    if  choice == 'y' :
        dice1 = random.randint(1 , 100)
        dice2 = random.randint(1, 100)

        print(f'{dice1}, {dice2}')
    else:
        print("error try again :")
