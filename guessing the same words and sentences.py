#!/usr/bin/env python
# coding: utf-8

# In[46]:


import time as t
p1_name = input("Please provide your Player1 name: ")
p2_name = input("Please provide your Player2 name: ")
print("Awesome! Lets jump in to the game")
p1_string = input("Please provide a word/sentence to guess: ")
p1_challenge_time = int(input("propose a challenge time(in mins): "))

hint1 = "The word starts with {letter}".format(letter =p1_string[0])

print("Hey {player2}! Your {challenge_time} minutes time starts now.. \nTic tic 1 \nTic tic 2 \n... \n...\nYour time starts now".format(player2 = p2_name,challenge_time = p1_challenge_time) )
start_time = time.perf_counter()

p2_guessing_input_string_updated = ''
i=0

while True:
    if(p2_guessing_input_string_updated == p1_string):
        end_time = time.perf_counter()
        total_time_taken = (end_time-start_time)/60
        print("You made it in {time_taken:0.2f} mins".format(time_taken = total_time_taken))
        break
    else:
        p2_guessing_input_string = input("lets guess the letter: ")
        if (p1_string[len(p2_guessing_input_string_updated)] == p2_guessing_input_string[0]):
            print("Letter {} is matching".format(len(p2_guessing_input_string_updated)+1))
            p2_guessing_input_string_updated =p2_guessing_input_string_updated + p2_guessing_input_string    
        else:
            print("Oh..We have to guess again!!")

if(total_time_taken < p1_challenge_time):
    print("{player} won the game".format(player = p2_name))
else:
    print("{player} won the game".format(player = p1_name))


# In[ ]:




