# Importing the array module
import array

# Creating an array (list) in Python
arr = array.array('i', [1, 2, 3, 4, 5])  # Combined into a single correct statement

# Accessing elements
print(arr[0])  # Output: 1
print(arr[2])  # Output: 3

# Modifying elements
arr[1] = 9
print(arr)  # Output: array('i', [1, 9, 3, 4, 5])  # it append 9 in array [1] which was 2 initially

# Appending an element
arr.append(6)  # Changed 'Append' to 'append'
print(arr)  # Output: array('i', [1, 9, 3, 4, 5, 6])  # append 6 after 5

# Removing an element
arr.remove(9)
print(arr)  # Output: array('i', [1, 3, 4, 5, 6])  # Remove 9 which is at index [1] 

# Popping an element
popped_element = arr.pop()
print(popped_element)  # Output: 6
print(arr)  # Output: array('i', [1, 3, 4, 5])  # removes number 6 from the array which is at index of [4]

# Finding the index of an element
index = arr.index(4)
print(index)  # Output: 2  # print the index of an array

# Reversing the array
arr.reverse()  # Changed 'Reverse' to 'reverse'
print(arr)  # Output: array('i', [5, 4, 3, 1])  # print array in reverse

# Extending the array
arr.extend([8, 9])
print(arr)  # Output: array('i', [5, 4, 3, 1, 8, 9])

# Slicing the array
slice_arr = arr[1:4]  # Added a space after '='
print(slice_arr)  # Output: array('i', [4, 3, 1])  # it prints element at index 1,2,3 only.
