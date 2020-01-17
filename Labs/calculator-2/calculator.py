"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

token_dict= {"+":2, "-":2, "*":2, "/":2, "square":1, "cube":1, "pow":2, "mod":2, "x+":2, "cubes+":2, "q":0}

# Your code goes here
running = True
# repeat forever:
while running:
#     read input
    user_input= input("Please enter an operator and some numbers or q to quit>  ")
#     tokenize input
    token= user_input.split(" ")
    first_token= token[0]
    if first_token not in token_dict:
        print ("This is not a valid input, please reenter below")
        continue
    elif len(token) < token_dict[first_token] + 1:
        print ("This is not a valid number of arguments, please reenter below")
        continue
#    print (first_token)
#     if the first token is "q":
#         quit
    elif first_token == "q" or first_token == "quit":
        running = False
#   else:
    else:
        if first_token == "+":
            print(add(float(token[1]), float(token[2])))

        elif first_token == "-":
            print(subtract(float(token[1]), float(token[2])))

        elif first_token == "*":
            print(multiply(float(token[1]), float(token[2])))

        elif first_token == "/":
            print(divide(float(token[1]), float(token[2])))
        
        elif first_token == "square":
            print(square(float(token[1]), float(token[2])))
        
        elif first_token == "cube":
            print(cube(float(token[1]), float(token[2])))
        
        elif first_token == "pow":
            print(power(float(token[1]), float(token[2])))

        elif first_token == "mod":
            print(mod(float(token[1]), float(token[2])))

        elif first_token == "x+":
            print(add_mult(float(token[1]), float(token[2])))

        elif first_token == "cubes+":
            print(add_cubes(float(token[1]), float(token[2])))