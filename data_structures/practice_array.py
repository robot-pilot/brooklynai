import array

array_data = array.array('i', [88,2,3,4])

print(array_data[0])

array_data[0] = 10

print(array_data[0])

array_data.append(77)
array_data.extend([4,5,6])

test_a = array_data.remove(2)
test_b = array_data.pop()

[print(i, end=' ') for i in array_data]

print()

print(test_a, test_b)

list_array = array_data.tolist()

print(list_array)


