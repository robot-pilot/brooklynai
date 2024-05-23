import string

def is_palindrome(s: str) -> bool:
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove punctuation, convert to lower case, and remove spaces
    clean_input = s.translate(translator).replace(" ", "").lower()
    
    # Check if the cleaned string is a palindrome
    left, right = 0, len(clean_input) - 1
    
    while left < right:
        if clean_input[left] != clean_input[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example usage
test_string = "A man, a plan, a canal, Panama!"
print(is_palindrome(test_string))  # Output should be True
