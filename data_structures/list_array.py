import sys
import array

# Create a list of integers
list_data = [1, 2, 3, 4, 5]

# Create an array of integers
array_data = array.array('i', [1, 2, 3, 4, 5])

# Get the size of the list
list_size = sys.getsizeof(list_data)
list_elements_size = sum(sys.getsizeof(item) for item in list_data)

# Get the size of the array
array_size = sys.getsizeof(array_data)

print(f"List size: {list_size} bytes")
print(f"List elements size: {list_elements_size} bytes")
print(f"Total List size: {list_size + list_elements_size} bytes")

print(f"Array size: {array_size} bytes")