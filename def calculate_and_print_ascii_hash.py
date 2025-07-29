def calculate_and_print_ascii_hash(input_string):
    
    total_ascii_sum = 0
    for char in input_string:
        ascii_value = ord(char)
        total_ascii_sum += ascii_value

    simple_hash = total_ascii_sum % 1000 
    print(f"Sum of ASCII values: {total_ascii_sum}")

user_input = input("Enter a string: ")

calculate_and_print_ascii_hash(user_input)