#This is a COMMENT!!!
'''
This is a multi line comment
'''

first_name = "Daniel"
last_name = "Carroll"

# response = raw_input("Enter your Name   ")
# print "Hello, ",response

birth_year = 1985
current_year = 2014
age = current_year - birth_year
# print "You are "+ str(age) +" years old."

'''
budget = raw_input("How much money you got?   ")

if int(budget) >= 100:
    brand = "nike"
    # print "You can buy cool "+brand+" shoes"
elif int(budget) >= 50:
    # print "You should save for better shoes"
    pass
else:
    # print "No shoes for me."
    pass
'''
questions = ["Professors Name?", "Class name?"]

characters = ["Harry", "Hagrid", "Hermonie", "Ron"]
characters.append(raw_input(questions[1]))
# print characters[2]

movies = dict() #Create Dictionary object
movies = {"Harry Potter": "Voldemort", "The Departed":"Leo Decap"}
print movies["Harry Potter"]+" "+characters[4]

'''
#while loop------
i = 0
while i<9:
    print "The count is ", i
    i = i+1


#for loop------
for i in range (0,10):
    print "The count is ", i
    i = i+1
'''

# #"FOR EACH" Loop-----
# rappers = ["Tupac", "Biggie", "JaRule"]
# for r in rappers:
#     # print "One of the best rappers is "+r
#     pass
#
# #FUNCTIONS-------------
# x = 2
#
# def calcArea(h, w):
#     area = h * w
#     return area + x
#
# a = calcArea(20, 100);
# # print "My area is "+str(a)+" sq feet."
# print a
#
# title = "Contact Us"
# body = "You can contact us at Contact@us.com"
# message = '''
# <!DOCTYPE HTML>
# <html>
#     <head>
#         <title>{title}</title>
#     </head>
#     <body>
#         {body}
#     </body>
# </html>
# '''
# message = message.format(**locals())
# print message
