str_1='shehri'
str_2='yar'
age = 20
full_name=str_1+str_2       # This is simple string concatination
print("My name is : ", full_name)

full_name += str(age)       # This is string interpolation
print ("My name and age is : ", full_name)

name_and_age = f'My name is {full_name} and I"m {age} year old.'    #This f-sting stand for formatted string
print (name_and_age)

my_str = 'Hello world'
print (my_str[0])       # This is string slicing we accessing it through index
print (my_str[3])
print (my_str[-1])      #It will start from the backside and print d

print (my_str[1:4])     #Now we are slicing the string string[start:end]


print(my_str[:7])  # Hello w
print(my_str[8:])  # rld
print(my_str)  # Hello world
 
# string[start:stop:step]  there's also an optional step parameter, which is used to specify the increment between each index in the slice.

print (my_str[0::2])

#to reverse a string

print (my_str[::-1])