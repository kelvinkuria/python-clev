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
       
def say_my_name_2(name):
    print(name)
# say_my_name_2('Kuria')
    
def greeting(greet,name):
    print(f'{greet} {name}!')
greeting('aloha', 'kuria')
