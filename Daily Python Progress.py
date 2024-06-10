'''
#Day - 1     DayCode-000567

# (# is a single line comment)
# (\''' is a multi line line comment \''')
# This is my first program

print("Hey i am a good boy")

# Escape sequence (\n) no space after an escape sequence

print("I am a good boy \nBut sometimes being bad is also exciting and new experience")

# What if we want to use double quote again inside a print(\" "\)

print("I am a \"good boy.\"\nand this viewer is also a good boy")

# We can write more on print statement
# sep will specify to seperate with the desired seperator like ~ , =
# end will put  000 after the end of the print function
print("Hey", 6, 7, sep="~", end=" 000\n")
print("Shrijan")

#Day - 2     DayCode-000678
#Data types

a = 123444
print(a)
b = "Shrijan"
print(b)
a1 = 9
print(a + a1)
c = True

#type() is used to find out the value of data

print("The type of a is", type(a))
print("The type of b is", type(b))
print("The type of c is", type(c))

#list is like an array which is changable (mutable)
#tuple is a list whoose value cannot be changed (unmutable)
#dict maps data with each other

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
tuple1 = [{"parrot","sparrow"}, {"lion","tiger"}]
dict1 = {"name":"Shrijan", "age":20, "canVote":True}

print(list1)
print(tuple1)
print(dict1)


#Day - 3    DayCode-000789
#Simple calculator

number1 = input("Enter a number:")
number2 = input("Enter a number:")
Input = input("What do you want to calculate for addition = 1, subtraction = 2, multiplication = 3 and division = 4:")

if Input == 1:
   print(number1 + number2)
elif Input == 2:
   print(number1 - number2)
elif Input == 3:
   print(number1 * number2)
else Input == 4:
   print(number1 / number2)

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))
operation = int(input("What do you want to calculate? Addition = 1, Subtraction = 2, Multiplication = 3, Division = 4: "))

if operation == 1:
    print(number1 + number2)
elif operation == 2:
    print(number1 - number2)
elif operation == 3:
    print(number1 * number2)
elif operation == 4:
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation choice.")

'''

#Day- 4    DayCode-000891

