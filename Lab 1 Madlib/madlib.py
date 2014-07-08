#Instructor Name
#Class Name
#AGE
#Plural Noun
#SECONDS I CAN HOLD BREATH
#mode of transportation
#Body Part
#ACTIVITIES FOR GRANDPARENTS



# Dear PROFESSORS NAME
# I am currently in your CLASS NAME class for the AGE time and I am wondering if I could get an extension on my homework about PLURAL NOUN.
# I wont be able to attend class for the next SECONDS I CAN HOLD BREATH weeks due to a MODE OF TRANSPORTATION accident.
# I also broke my BODY PART while ACTIVITIES FOR GRANDPARENTS so I am unable to operate the complexities of FSO 3.0.
# I feel EMOTION that you are giving me this exception, and if necessary ill give you $HOW MANY FINGERS to give me a 100 on this assignment.
# Sincerely,
# NICKNAME

answers = [] #Array to hold answers to questions

'''
raw_input queries user for an answer to the question inside parenthesis. answers.append adds the answer to the array named answers
'''
answers.append(raw_input("What is your instructors name?  "))
answers.append(raw_input("What is the name of the class?  "))
answers.append(raw_input("What is your current age?  "))
answers.append(raw_input("Enter a plural noun.  "))
answers.append(raw_input("How many seconds can you hold your breath?  "))
answers.append(raw_input("How do you normally travel long distances?  "))
answers.append(raw_input("Favorite body part?  "))
answers.append(raw_input("What do your grandparents do for fun?  "))
answers.append(raw_input("How does the dentist make you feel?  "))
answers.append(raw_input("How many fingers do you think I am holding up right now?  "))
answers.append(raw_input("Nickname your girlfriend/boyfriend calls you.  "))

story = dict() #Create Dictionary Object
story = {0: "Dear ", 1: " I am currently in your ", 2: " class for the ", 3: "  time and I am wondering if I could get an extension on my homework about ", 4: " I wont be able to attend class for the next ", 5: " weeks due to a ", 6: " accident. ", 7: " I also broke my ", 8: " while ", 9: " so I am unable to operate the complexities of FSO 3.0. ", 10: " I feel ", 11: " that you are giving me this exception, and if necessary ill give you $", 12: " to give me a 100 on this assignment.", 13: "Sincerely,"}
print story[1]