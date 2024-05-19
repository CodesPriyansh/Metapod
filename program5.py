#MyMagic8Ball 

import random 

#write answers
ans1 = "work hard."
ans2 = "learn skills."
ans3 = "find love."
ans4 = "hug your father."
ans5 = "retire your mother."
ans6 = "become strong."
ans7 = "die with no regrets."
ans8 = "write poetry." 

print("WelcomeToMyMagic8Ball.") 

#get the users name 
user_name = input("what's your name: \n")
#get the users question
question = input("Ask me for advice then press enter to shake me:\n") 
print("shaking..." * 4)

# use the randint() function to select the correct answer.

choice = random.randint(1, 8) 

if choice == 1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4 
elif choice== 5:
    answer = ans5
elif choice == 6:
    answer = ans6 
elif choice == 7:
    answer = ans7
else:
    answer = ans8
    
#print the answer to the screen
print(answer) 

input("press the enter to finish: \n") 
print("thanks for playing", user_name)




