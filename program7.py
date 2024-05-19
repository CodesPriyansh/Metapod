import random 
computer_number = random.randint(1, 100)
counter = 1

def guess_num(comp, user):
    if comp == user:
        result = "win"
    elif comp < user:
        result = "high"
    else: 
        result = "low"
    return result 
        
guess = int(input("guess the number: ")) 

fun = guess_num(computer_number, guess) 

while fun != "win":
    if fun == "low":
        guess = int(input("too low, try again: "))
        counter += 1
        
    elif fun == "high":
        guess = int(input("too high, try again."))
        counter += 1
    fun = guess_num(computer_number, guess) 
    
    
print('correct!:',computer_number, 'you guessed it in:', counter) 
        
        
         
        
        