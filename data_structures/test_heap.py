import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 23)
heapq.heappush(heap, 14)
heapq.heappush(heap, 55)
heapq.heappush(heap, 2)

print(f"Heap after inserting elements: {heap}")

smallest = heapq.heappop(heap)

print(f"Smallest: {smallest}")

print(f"Heap after: {heap}")

list_h = [2, 56, 1.9, 505, 44]

heapq.heapify(list_h)

print(f"heapify: {list_h}")

max_heap = []

heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -15)

print(f"Max heap {[-f for f in max_heap]}")
