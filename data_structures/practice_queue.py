from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

peek = queue[0]

print(peek)

[print(i, end=' ') for i in queue]

print()

queue.popleft()

[print(i, end=' ') for i in queue]