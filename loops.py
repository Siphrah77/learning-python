'''
LOOPS
- A loop occurs when the same process is executed repeatedly until a particular
set of conditions is met.

TYPES OF LOOPS IN PYTHON
1. while loop
2. for in loop
3. Nested loops

Components of a loop
1. Condition: This is the statement that determines if the loop should be executed. eg x < 7, it is usually a boolean statement: One that returns either a True of False value
2. Initializer: Contains a value that can later be incremented. By default the initializer should start at value 0
3. Incrementation: This is when the initialized value is incremented(+1) to be able to determine the number of loops done.

The components above in python will only apply to a while loop, however for a for in loop this will be different as will  be shown.
'''
# EXAMPLE 1
# While loop
i = 0 # initializer
while(i < 6): # The condition is placed inside the while() brackets
    print(f"Lap {i}")
    i += 1 # Incrementation. This is the same as saying i = i + 1

# NB: The i on the right hand side contains the initial value of i eg: 0

# EXAMPLE 2


while(True):
    username=input("Input your name:")
    print(username)
    if username =="x":
        break
    

    





















