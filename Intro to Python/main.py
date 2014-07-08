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

budget = raw_input("How much money you got?   ")

if int(budget) >= 100:
    brand = "nike"
    print "You can buy cool "+brand+" shoes"
elif int(budget) >= 50:
    print "You should save for better shoes"
else:
    print "No shoes for me."