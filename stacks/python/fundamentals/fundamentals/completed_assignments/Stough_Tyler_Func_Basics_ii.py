# Countdown
# Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    new_list = []
    for x in range(num,-1,-1):
        new_list.append(x)
    return new_list

print(countdown(10))
print(countdown(5))

#####################################################################################################################################

# Print and Return
# Create a function that will receive a list with two numbers. Print the first value and return the second.

# Example: print_and_return([1,2]) should print 1 and return 2

# create a function
# receives two arguments
def print_and_return(a = 0, b = 0):
    # print the first value
    print(a)

    # return the second value
    return(b)

print(print_and_return(1,2))

######################################################################################################################################

# First Plus Length
# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# create a function that accepts a list
def first_plus_length (list):
    sum = list[0] + len(list)

    # returns the sum of the first value + list's length
    return sum

print(first_plus_length([1,2,3,4,5]))
print(first_plus_length([4,2,3,4,5]))


########################################################################################################################################

# Values Greater than Second 
# Write a function that accepts a list and creates a new list containing only the values 
# from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# function that accepts a list
def values_greater_than_second(list):
    # early out
    if(len(list) <= 1):
        return False

    # creates a new list
    new_list = []

    #only add values that are greater than the second value of list
    for val in range(len(list)):
        if(list[val] > list[1]):
            new_list.append(list[val])
    # print how many values are in the new list
    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([5]))
print(values_greater_than_second([5,1,3,2,7,4]))

#########################################################################################################################################

# This Length, That Value 
# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.

# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_length_that_value (size, value):
    new_list = []

    for val in range(size):
        new_list.append(value)

    return new_list

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))