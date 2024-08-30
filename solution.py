my_list = [] # create an empty list

# Add elements to the list

# crating a tuple to hold the items to be added to the list
items = (10, 20, 30, 40)

# loop through the tuple and add each item to the list
for item in items:
    my_list.append(item)

# Add 15 at the second position of the list
my_list.insert(1, 15)

# Extending the list with another list
extending_list = [50, 60, 70] # create a list extending_list to be added to the my_list
my_list.extend(extending_list) # extending my_list with the extending_list list

# Remove the last element from the list
my_list.pop() # remove the last element from the list

# Sorting the list
my_list.sort() # sorting the list my_list in ascending order

# Finding and printing the index of 30 in the list my_list
index_of_30 = my_list.index(30) # finding the index of 30 in the list my_list
print(f"The index of 30 in the list my_list is {index_of_30}") # printing the index of 30 in the list my_list
