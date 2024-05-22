from typing import Dict
from collections import deque
from dataclasses import dataclass, field

@dataclass
class Gr:

	"""Summary
	"""
	
	graph: dict = field(default_factory=dict)

gr = Gr()
gr.graph = {
	"A": ["B", "C"],
	"B": ["A", "D", "E"],
	"C": ["A", "F"],
	"D": ["B"],
	"E": ["B", "F"],
	"F": ["C", "E"]
}

def bfs(graph: Dict, start: str) -> None:
	"""Summary
	
	Args:
	    graph (Dict): Description
	    start (str): Description
	"""

	visited = set()
	queue = deque([start])
	while queue:
		vertex = queue.popleft()
		if vertex not in visited:
			print(vertex)
			visited.add(vertex)
			queue.extend(set(graph[vertex]) - visited)

def dfs(graph: Dict, start: str) -> None:
    """Summary
    
    Args:
        graph (Dict): Description
        start (str): Description
    """

    visited = set()
    stack = deque([start])
    while stack:
    	vertex = stack.pop()
    	if vertex not in visited:
    		print(vertex)
    		visited.add(vertex)
    		for neighbor in reversed(graph[vertex]):
    			if neighbor not in visited:
    				stack.append(neighbor)

if __name__ == "__main__":
	bfs(gr.graph, "A")
	print()
	dfs(gr.graph, "A")
