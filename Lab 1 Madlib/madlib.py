def money_maker(age, fingers):
    total = int(age)-int(fingers)
    if total >=0:
        total=1
        return total
    else:
        total=2
        return total

answers = [] #Array to hold answers to questions
final_story = "Placeholder"
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
story = {0: "Dear ", 1: " I am currently in your ", 2: " class for the ", 3: "th time and I am wondering if I could get an extension on my homework about ", 4: " I wont be able to attend class for the next ", 5: " weeks due to a ", 6: " accident. ", 7: " I also broke my ", 8: " while ", 9: " so I am unable to operate the complexities of FSO 3.0. ", 10: " I feel ", 11: " that you are giving me this exception, and if necessary ill give you $", 12: " to give me a 100 on this assignment.", 13: "Sincerely,"}


line_number = 0
while line_number < 12:
    if line_number == 0:
        final_story = story[line_number]+answers[line_number]
        print final_story
        line_number += 1
    elif line_number > 0 and int(line_number) < 3:
        final_story = story[line_number]+answers[line_number]+story[line_number+1]+answers[line_number+1]+story[line_number+2]+answers[line_number+2]+"."
        print final_story
        line_number += 3
    elif line_number == 4:
        final_story = story[line_number]+answers[line_number]+story[line_number+1]+answers[line_number+1]+story[line_number+2]
        print final_story
        line_number += 3
    elif line_number == 7:
        final_story = story[line_number]+answers[line_number-1]+story[line_number+1]+answers[line_number]+story[line_number+2]
        print final_story
        line_number += 3
    elif line_number == 10:
        final_story = story[line_number]+answers[line_number-2]+story[line_number+1]+str(money_maker(answers[2],answers[9]))+story[line_number+2]
        print final_story
        line_number += 1
    elif line_number == 11:
        print story[13]
        print answers[10]
        line_number += 1
    else:
        pass