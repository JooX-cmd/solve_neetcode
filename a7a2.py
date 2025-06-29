# import random 
# get  two  input form user   
# check int not str 
#hight  or low  
# print  to string 
#get random 
#
# check if number 

import random 

number = random.randint(1, 200)
#loop 
while True :
# erroe handel or expion 
    try:
        guess = int(input('Gess the number bet 1 to 200: ')) 
        if guess == number:
            print(' u guessd the number ')
        elif guess < number:
            print('tow low')
        else:
            print('to high')
    except ValueError:
        print('plz enter  number int not str')