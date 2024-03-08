#Boolean Expressions
#If...else
#If....else..if

#Boolean data types(true,false)
# #weather app
# weather = input("Kuko aje (What's the weather like?): ")

# if weather == 'rain':
#     print('Bring an umbrella!')
# elif weather == 'cloudy':
#     print('No need for a coat.')
# else:
#     print('Dress according to the weather.')

# one equal sign(=) used to assign values
# two equal signs(==) is a comparison operator(==,<.>,<=,=>)

# Grades app

#  score = 78

# if score >= 90:
#     print('Wow, you passed with flying colors!')
# elif 80 <= score < 90:
#     print('You did great!')
# elif 70 <= score < 80:
#     print('Try harder next time.')
# elif 60 <= score < 70:
#     print('Pull up your socks!')
# else:
#     print('You need to study more.')


# if score >= 60 and score <=100:
#            print('pass')


# Functions - a block of code that performs a specific task. It enables reusability of code modularity and better organisation.
#Arguments are values passed to a function when it is called.
# parameters are temporary placeholders for arguments
# def say_my_name():
#        print('Kuria')

# say_my_name()
       
#def say_my_name_2(name):
   # print(name)
# say_my_name_2('Kuria')
    #multiple arguments in a functtion
#def greeting(greet,name):
    #print(f'{greet} {name}!')
#greeting('aloha', 'kuria')

#default arguments are passed in if said arguments are not passed in


# def greeting(name='kush', greet = 'Hey'):
#   print(f'{greet}, {name}!')

# greeting()

#take 2 integers amd returns their sum
# def sum(a,m):
    
#     return a + m

# print(sum(1,2))

#def calculateFoodTotal(food_amount, tip_percentage):
"""Calculates the total cost of food including tip.

  Args:
      food_amount (float): The cost of the food.
      tip_percentage (float): The tip percentage as a number (e.g., 15 for 15%).

  Returns:
      float: The total cost including tip.
  """
#   tip = food_amount * (tip_percentage / 100)
#   total = food_amount + tip
#   return f"Total cost: ${total:.2f}"  # String formatting for currency

# # Example usage
# print(calculateFoodTotal(100, 45))

    


def suggest_clothing(weather):
  """Suggests clothing based on the weather condition.

  Args:
      weather (str): The weather condition (rain, cloudy, etc.).

  Returns:
      str: A message suggesting clothing based on weather.
  """
  if weather == 'rain':
    return 'Bring an umbrella!'
  elif weather == 'cloudy':
    return 'No need for a coat.'
  else:
    return 'Dress according to the weather.'

# Example usage
weather = 'cloudy'
clothing_suggestion = suggest_clothing(weather)
print(clothing_suggestion)
  
  

