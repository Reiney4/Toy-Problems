#create a function is_consonant
def is_consonant(char):
    return char.isalpha() and char not in "aeiou"

#created a function to calculate the ASCII value of the constant according to alphabetic order
def get_consonant_value(char):
    return ord(char) - ord('a') + 1

# created a function that iterates through the input string to get  the maximum value of calculation

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

#added an input string to run the code
input_string = "valerie"
result = highest_consonant_value(input_string)
print(result) 