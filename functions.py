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


