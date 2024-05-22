def binary_search(arr, search, low, high):
	if low > high:
		return f"{search} not found"

	mid = (low + high) // 2

	if arr[mid] == search:
		return mid
	elif arr[mid] < search:
		binary_search(arr, search, mid+1, high)
	else:
		binary_search(arr, search, low, mid-1)



arr = [1,2,6,19,34,56,89,901]
search = 19
idx = binary_search(arr, search, 0, len(arr)-1)
if idx: print(f"{search} found at idx {idx}")
else: print(f"{search} not found")