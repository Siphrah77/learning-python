list_example=["one","two","three","four","four","three"]
set_example={"one","two","three","four","four","three"}
tuple_example_one=("one","two","three","four","four","three")
tuple_example_two="one","two","three","four","four","three"
'''
# To find out the type of a variable we use the inbuilt function type() 
which takes in a variable as its argument and returns the datatype of our 
variable.
'''
# list example

print(type(list_example))
print(type(set_example))
print(type(tuple_example_one))
print(type(tuple_example_two))

print(list_example)
print(set_example)
print(tuple_example_one)
print(tuple_example_two)

'''
LIST
-A list can take in any datatype,it also indexes each item inside it
'''

# Adding items at the end of our list
list_example.append("six")
print(f"EDITED LIST_EXAMPLE:{list_example}")

# getting the number of items in a list
print(len (list_example))

# getting maximum value in a list
list_b=[10,6,88,0]
# getting maximum value in a list
print(max(list_b))

# getting minimum value in a list
print(min(list_b))

# getting a particular item by its index
# NB:indexing in collection will always start at 0
print(list_example[-2])

# modifying an item in our list
list_example[-1]="ten"
print(list_example)

# removing an item from a list
# removing an item with a particular value
list_example.remove("ten")
print(list_example)

# removing an item at the end of our list
list_example.pop()
print(list_example)

# iterating through our list items
# We iterate through our list using the for...in loop
for item in list_example:
    print(f"Item {item}")




