# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.


def hello() :
     print("Hello, user!")


# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
     
def pack( arg1, arg2, arg3) :
     return [arg1, arg2, arg3]
  





# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)



# Test the functions
print("Testing hello():")
hello()

print("\nTesting pack():")
print(pack("apple", "banana", "orange"))

print("\nTesting eat_lunch():")
eat_lunch(["sandwich", "chips", "apple"])

print("\nTesting eat_lunch():")
eat_lunch([])