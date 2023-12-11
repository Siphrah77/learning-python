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
    
# how to add a n item at the beginning of our list


list_example.insert(0,"fifty")
print(f"MODIFIED LIST={list_example}")


# SET OPERATIONS

# union:combines the common
first_set={1,2,3,4,5,6}
second_set={4,5,6,7,8,9}

union_first_second_set=first_set.union(second_set)
print(union_first_second_set)

alternative_combined_set=first_set| second_set
print(alternative_combined_set)

# intersection:takes the common items in sets

my_intersection=first_set.intersection(second_set)
print(my_intersection)

alternative_intersection=first_set & second_set
print(alternative_intersection)

# Set diifference:This is used to check items that are in one list and not in the other
# E.G in the example below,this will check for items in the first that are not in the second
set_difference=first_set.difference(second_set)

alterative_set_difference=second_set-first_set
print(alterative_set_difference)

# python Dictionaries:They store items with keys and values
student1={
    "firstname":"johnte",
    "secondname":"kimani",
    "age":25,
    "is_married":False
}
student2={
    "firstname":"Carol",
    "secondname":"Wanjira",
    "age":25,
    "is_married":True
}
print(student1["firstname"])

student=[student1,student2]
for student in student:
    print(f"FIRST NAME={student['firstname']},SECOND NAME={student['secondname']}")
    
    
# dictionary operations
# 1.Addition
student1["id"]=190

print(student1)

# 2.Getting/Reading our dictionary
student_id = student1["id"]
print(student_id)

alternartive_student_id = student1.get("id")
print(alternartive_student_id)

# Updating 
student1["id"]=9001
print(student1["id"])


# Deleting an item from a dictionary
student1.pop("id")
print(student1)












