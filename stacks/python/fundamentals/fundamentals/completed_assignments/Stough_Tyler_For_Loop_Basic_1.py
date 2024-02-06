# Basic
# Print all integers from 0 to 150.
for i in range(151):
    print(i)


# Multiples of Five
# Print all the multiples of 5 from 5 to 1,000
for j in range(5,1001,5):
    print(j)


# Counting, the Dojo Way
# Print integers 1 to 100. 
for k in range(1,101):

# If divisible by 5, print "Coding" instead. 
    if (k % 5 == 0 and k%10 != 0):
        print('Coding')

# If divisible by 10, print "Coding Dojo".
    elif (k % 10 == 0):
        print('Coding Dojo')

    else:
        print(k)


# Whoa. That Sucker's Huge
# Add odd integers from 0 to 500,000, and print the final sum.
def huge_num():
    sum = 0
    for l in range(1,500000,2):
        sum = sum + l
    return sum

print(huge_num())


# Countdown by Fours
Print positive numbers starting at 2018, counting down by fours.
for m in range(2018,0,-4):
    print(m)


# Flexible Counter
# Set three variables: lowNum, highNum, mult.
lowNum = 1
highNum = 20
mult = 5

# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
    # For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
for n in range(lowNum, highNum + 1):
    if(n % mult == 0):
        print(n)

