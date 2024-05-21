from typing import Dict

def print_hash(hashmap: Dict) -> None:
	"""prints hash to schreen
	
	Args:
	    hashmap (Dict): hashmap to print
	"""
	for key, value in hashmap.items():
		print(f"{key}: {value}")
	print()


hashmap = {"one": 1, "two": 2, "three":3}

print(hashmap)
print(hashmap["one"])
del hashmap["one"]
print(hashmap)
print()

print_hash(hashmap)

print(hashmap.get('four', 4))
print()

print_hash(hashmap)

print(hashmap.setdefault('four', 4))
print()

print_hash(hashmap)