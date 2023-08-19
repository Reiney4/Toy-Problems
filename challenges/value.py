#create a function is_consonant
def is_consonant(char):
    return char.isalpha() and char not in "aeiou"

def get_consonant_value(char):
    return ord(char) - ord('a') + 1

def highest_consonant_value(s):
    max_value = 0
    current_value = 0

    for char in s:
        if is_consonant(char):
            current_value += get_consonant_value(char)
            max_value = max(max_value, current_value)
        else:
            current_value = 0

    return max_value

# Example usage
input_string = "abcdedfg"
result = highest_consonant_value(input_string)
print(result)  # Output: 15 (consonant substrings: "bcd", "d", "fg")
