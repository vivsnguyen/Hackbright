"""Restaurant rating lister."""


# put your code here
def format_restaurant_data(file_name):

    log_file = open(file_name)

    formatted_list_of_file = []

    for line in log_file:
        line = line.rstrip()
        line = line.split(":")
        formatted_list_of_file.append(line)

    return formatted_list_of_file

def create_restaurant_dict(file_name):

    formatted_list_of_file = format_restaurant_data(file_name)

    restaurant_dict = {}

    for line in formatted_list_of_file:
        restaurant_dict[line[0]] = line[1]

    return restaurant_dict

# print(create_restaurant_dict("scores.txt"))

# def print_alpha_dict(file_name):

#     restaurant_dict = create_restaurant_dict(file_name)

#     for restaurant in sorted(restaurant_dict.keys()):
#         print(f'{restaurant} is rated at {restaurant_dict[restaurant]}.')

def print_alpha_dict(restaurant_dict):

    for restaurant in sorted(restaurant_dict.keys()):
        print(f'{restaurant} is rated at {restaurant_dict[restaurant]}.')

# print_alpha_dict('scores.txt')

# def interactive_restaurant_ratings(restaurant_dict):

#     user_action = input("""
#         Press s to see all the ratings in alphabetical order.
#         Press a to add and review a new restaurant.
#         Press q to quit.
#         >""")


#     if user_action == "s":
#         print_alpha_dict(restaurant_dict)
#         interactive_restaurant_ratings(restaurant_dict)

#     elif user_action == "a":
#         user_restaurant = input('Enter the restaurant name.')
#         user_rating = int(input('Enter the rating.'))
#         if user_rating > 5 and user_rating < 1:
#             print('Enter a number between 1 and 5.')


#         restaurant_dict[user_restaurant] = user_rating
#         interactive_restaurant_ratings(restaurant_dict)

#     elif user_action == 'q':
#         print('Goodbye! Thanks for rating.')

#     else:
#         print('Enter a valid input.')
#         interactive_restaurant_ratings(restaurant_dict)
        
def interactive_restaurant_ratings(restaurant_dict):

    running = True

    while running:
        user_action = input("""
        Press s to see all the ratings in alphabetical order.
        Press a to add and review a new restaurant.
        Press q to quit.
        >""")

        if user_action == "s":
            print_alpha_dict(restaurant_dict)
            continue

        elif user_action == "a":
            user_restaurant = input('Enter the restaurant name. ')
            user_rating = int(input('Enter the rating. '))

            while user_rating > 5 or user_rating < 1:
                user_rating = int(input('Enter a number between 1 and 5. '))

            restaurant_dict[user_restaurant] = user_rating

        elif user_action == 'q':
            print('Goodbye! Thanks for rating.')
            running = False

        else:
            print('Enter a valid input.')
            



interactive_restaurant_ratings(create_restaurant_dict('scores.txt'))