str_1='shehri'
str_2='yar'
age = 20
full_name=str_1+str_2       # This is simple string concatination
print("My name is : ", full_name)

full_name += str(age)       # This is string interpolation
print ("My name and age is : ", full_name)

name_and_age = f'My name is {full_name} and I"m {age} year old.'    #This f-sting stand for formatted string
print (name_and_age)