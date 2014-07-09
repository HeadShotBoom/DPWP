#Below is a function i will use to take user input from multiple entries and calculate a value to return in the madlib
def money_maker(age, fingers):
    total = int(age)-int(fingers)
    #This is a conditional statement that allows me to account for negative numbers
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

# story = dict() #Create Dictionary Object
'''
I broke up the pregenerated part of my madlib into numbered entries of the following dictionary. I seperated the madlib where the blanks would
be in a normal madlib. This allows me to seamlessly assemble the madlib for easy reading later
'''
story = {0: "Dear ", 1: " I am currently in your ", 2: " class for the ", 3: "th time and I am wondering if I could get an extension on my homework about ", 4: " I wont be able to attend class for the next ", 5: " weeks due to a ", 6: " accident. ", 7: " I also broke my ", 8: " while ", 9: " so I am unable to operate the complexities of FSO 3.0. ", 10: " I feel ", 11: " that you are giving me this exception, and if necessary ill give you $", 12: " to give me a 100 on this assignment.", 13: "Sincerely,"}

'''
This is a counter for purposes of ensuring the loop runs through in its entirely. It will also be used to interate through
the dictionary entries later and answers array during assembly
'''
line_number = 0


while line_number < 12:#This is my while loop for assembling the madlib it will run as long as line_number is less than 12
    '''
    I used conditional statements to assemble the madlib. I didnt want the text to read on a single line, but more like a childs
    note would read.
    '''
    if line_number == 0:
        final_story = story[line_number]+answers[line_number] #Concationate Line 0 from the story and answer 0 from the array.
        print final_story #Prints the variable
        line_number += 1 #interates the line number so that it will run the next section of code.
    elif line_number > 0 and int(line_number) < 3: #This could have been simplified, but I wanted to use a logical operator for rubric purposes
        final_story = story[line_number]+answers[line_number]+story[line_number+1]+answers[line_number+1]+story[line_number+2]+answers[line_number+2]+"."
        '''
        Since I overwrite the final_story variable above, I can simply reprint it without repeating the first lines text.
        '''
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
        '''
        If one of the conditions above fails, we will enter this section of code and cause the function to stop
        '''
        pass

