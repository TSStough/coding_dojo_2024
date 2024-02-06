num1 = 42 #variable declaration, numbers
num2 = 2.3 #variable declaration, number / float
boolean = True #variable declaration, boolean
string = 'Hello World' #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list, strings, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary, string, number, boolean, initialize
fruit = ('blueberry', 'strawberry', 'banana') #tuple, string, initialize
print(type(fruit)) #log statement, type check, string
print(pizza_toppings[1]) #log statement, list, access value
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #log statement, dictionary, access value
person['name'] = 'George' #dictionary, access value, change value
person['eye_color'] = 'blue' #dictionary, access value, change value
print(fruit[2]) #log statement, dictionary, access value

if num1 > 45: #if, variable, number
    print("It's greater") #log statement, string
else: #else
    print("It's lower") #log statement, string

if len(string) < 5: #if, length check, string, number
    print("It's a short word!") #log statement, string
elif len(string) > 15: #else if, length check, string, number
    print("It's a long word!") #log statement, string
else: #else
    print("Just right!") #log statement, string

for x in range(5): #for loop, variable declaration, sequence, stop, number
    print(x) #log statement, variable/number
for x in range(2,5): #for loop, variable declaration, sequence, start, stop, numbers
    print(x) #log statement, variable/number
for x in range(2,10,3): #for loop, variable declaration, sequence, start, stop, increment, numbers
    print(x) #log statement, variable
x = 0 #variable declaration, number
while(x < 5): #while loop, variable, start, stop
    print(x) #log statement, variable/number
    x += 1 #variable, increment, number

pizza_toppings.pop() #list, function, parameter
pizza_toppings.pop(1) #list, function, parameter, number

print(person) #log statement, dictionary
person.pop('eye_color') # dictionary, function, parameter, delete value, string
print(person) #log statement, dictionary

for topping in pizza_toppings: #for loop, declared variable, list
    if topping == 'Pepperoni': #if, variable, boolean, string
        continue #continue
    print('After 1st if statement') #log statement, string
    if topping == 'Olives': #if, variable, boolean, string
        break #break

def print_hello_ten_times(): #function, argument
    for num in range(10): #for loop, declare variable, sequence, stop, number
        print('Hello') #log statement, string

print_hello_ten_times() #function, argument

def print_hello_x_times(x): #function, argument
    for num in range(x): #for loop, declare variable, sequence, stop, variable
        print('Hello') #log statement, string

print_hello_x_times(4) #function, argument, number

def print_hello_x_or_ten_times(x = 10): #function, argument, variable declared
    for num in range(x): #for loop, declare variable, sequence, stop, variable
        print('Hello') #log statement, string

print_hello_x_or_ten_times() #function, argument
print_hello_x_or_ten_times(4) #function, argument, number


"""
Bonus section
"""

# print(num3) #log statment, variable
# num3 = 72 #declare variable
# fruit[0] = 'cranberry' #tuple, access value, number
# print(person['favorite_team']) #log statement, dictionary, access value, string
# print(pizza_toppings[7]) #log statement, list, access value
#   print(boolean) #log statement, boolean
# fruit.append('raspberry') #tuple, add value, string
# fruit.pop(1) #tuple, remove value, number