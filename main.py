import random

#  here we set the value of email that we gonna format
email = "ismailbouzarhoun@gmail.com"
# here we set the value of number of points that we want between caracters
number_of_point = 5
# here we set the number of digits that we want in the random number
input_number_of_digits = 3


# this function for randomize number
def random_number(number_of_digits):

    #this give you the the smallest number for number of digits you enter 
    smallest_number = 10 ** (number_of_digits - 1)
    #this give you the the biggest number for number of digits you enter 
    Biggest_number = (10 ** number_of_digits) - 1
    # and this randomize the number between smallest number and biggest number that has number of digits that you enter
    random_number = random.randint(smallest_number, Biggest_number)
    return random_number
# this to refer the number of digits to the function
num = random_number(input_number_of_digits)
# the end of function


# this split the code to to part usename part that come before @ and this is the part that we gonna randomize the points
characters = list(email.split("@")[0])
# this randomize the position of the points in the mail and this function tale 3 parametres the first where to start the randomize, and where to end, and the number numbers that we randomize  
random_points = random.sample(range(1, len(characters)), number_of_point)
# and here  we gonna sort these postion
random_points.sort()
# and here we add this points to the mail with this position that we randomize
for point in random_points[::-1]:
    characters.insert(point, '.')
random_email = ''.join(characters)

# here we call the random number from the firs function
random_number = num
random_number_string = str(random_number)
# here we format the mail to give us the final one
new_mail = random_email + "+" + random_number_string + email.split("@")[1]
print(new_mail)
