string = "abcd"

def reverse_string(string):
	if len(string) == 0:
		return string
	else:
		return string[-1] + reverse_string(string[0:-1])

print(reverse_string(string))


string = 'racecap'

def is_palindrome(string):
	if len(string) <= 1:
		return True
	else:
		return string[0] == string[-1] and is_palindrome([string[1:-1]])

print(is_palindrome(string))
