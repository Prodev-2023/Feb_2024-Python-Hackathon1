# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.

age = int(input("please Enter your age here"))
# - Uses a conditional statement to check if the age is greater than or equal to 18.

if age >= 18:
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
    print(f"At age {age} you are eligible to vote")
else:
     
     print(f"At age {age} you are not eligible to vote")
