def add(num1, num2):
    return num1 + num2
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
#select options
print("Please select operation -\n" \
        "1. Add\n" \
         "2. sub\n"  )


# Take input from the user 
select = int(input("Select operations:"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

else:
    print("Invalid input")