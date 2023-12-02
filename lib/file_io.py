def write_file(file_name, file_content):
    # Open file with 'w' mode to write content to it
    with open(f"{file_name}.txt", 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Open file with 'a' mode to append content to it
    with open(f"{file_name}.txt", 'a') as file:
        file.write(append_content)  # Append content without a new line

def read_file(file_name):
    # Open file with 'r' mode to read content from it
    with open(f"{file_name}.txt", 'r') as file:
        content = file.read()
        return content

