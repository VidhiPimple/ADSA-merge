def ascii_hash(input_string,size):
    
    total_ascii_sum = 0
    for char in input_string:
        ascii_value = ord(char)
        total_ascii_sum += ascii_value

    simple_hash = total_ascii_sum % size 
    print(f"Sum of ascii values: {total_ascii_sum}")
    print(f"Calculated hash: {simple_hash}")

user_input = input("Enter a string: ")
size = int(input("Enter hash table size:"))
ascii_hash(user_input,size)
