#   Create a Python program using a custom module that asks the user how they are feeling today,
#   and responds with a custom message based on the mood entered.
#   Give responses for 'happy', 'sad', 'okay', and whatever else you want.

# Code Example:

# # moody.py
# def mood_response(mood):
#     # Implement your response logic here

# # main.py
# import moody
# mood = input("How are you feeling today? ")
# print(mood_responses.mood_response(mood))


# def mood_response(mood):
#     if mood == 'happy':
#         print('happy is good')
#     elif mood == 'sad':
#         print('sad is not good')
#     elif mood == 'okay':
#         print('okay is okay')
#     else:
#         print('invalid input, try again')

import mood
mood1 = input("How do you feel today? ")
print(mood.mood_response(mood1))




#   im most likely doing this all wrong, but when i try to import (on line 27) it says file not found, but that is in fact the proper file name. i no understand :P