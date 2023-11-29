def say_hello():
    print("Hello!!!")
def addition(x,y):
    results =x+y
    return results
add_results=addition(10,11)
print(add_results)

# subtraction,multiplacation,isEven,division
def subtraction(x,y):
     results=x-y
     return results
subtract_results=subtraction(15,10)
print(subtract_results)

def multiplacation(x,y):
    results=(x*y)
    return results
multiply_results=multiplacation(5,2)
print(multiply_results)

def is_even(x):
    if(x%2==0):
        return True
    return False
results=is_even(13)
print(f"Is Even={results}")

def division(x,y):
    results=(x/y)
    return results
division_results=division(9,3)
print(division_results)


# def is_divisible(x,y):
#     if(x%y==0):
#         return True
#     return False
# results=is_divisible(10,2)
# print(f"Is Divisible={results}")


def divisible(x,y):
    if(x%y==0):
        return f"{x} is divisible by {y}"
    return f"{x} is not divisible by {y}"

print("CHECK DIVISIBILTY BETWEEN 'X' AND 'Y'/n")
print("Press 'x' to exit ")

while (True):
    x=input("input value for X:")
    if x.upper()=="X":
        break
    y=input("input value for Y:")
    
    if x.isdigit() and y.isdigit():
        input_x=int(x)
        input_y=int(y)
        results=divisible(input_x,input_y)
        print(results)
    else:
        print("INVALID INPUTS,TRY AGAIN")




