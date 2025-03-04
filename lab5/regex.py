import re

# Function to check if a string starts with 'a' followed by any number of 'b's
def check_pattern1(text):
    return bool(re.fullmatch(r'a*b*', text))

# Function to check if a string starts with 'a' followed by 2 or 3 'b's
def check_pattern2(text):
    return bool(re.fullmatch(r'ab{2,3}', text))

# Function to find lowercase words connected with underscores
def find_underscore_words(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)

# Function to find uppercase words followed by lowercase letters
def find_camelcase_words(text):
    return re.findall(r'\b[A-Z][a-z]+\b', text)

# Function to check if a string starts with 'a' and ends with 'b'
def check_start_end(text):
    return bool(re.fullmatch(r'a.*b', text))

# Function to replace spaces, commas, and dots with colons
def replace_special_chars(text):
    return re.sub(r'[ ,.]', ':', text)

# Function to convert snake_case to camelCase
def snake_to_camel(text):
    words = text.split('_')
    return words[0] + ''.join(w.capitalize() for w in words[1:])

# Function to split a string at uppercase letters
def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

# Function to insert spaces between capitalized words
def space_out_capitals(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# Function to convert camelCase to snake_case
def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

