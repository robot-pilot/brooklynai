def quick_sort(arr):
	if len(arr) <=1:
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quick_sort(left) + middle + quick_sort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr))

print()
print()

def merge_sort(arr):
	# print(arr)
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	print(len(arr), mid, arr[:mid], arr[mid:])
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])

	return merge(left, right)

def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result

arr = [3, 6, 8, 10, 1, 2, 1]
print(merge_sort(arr))