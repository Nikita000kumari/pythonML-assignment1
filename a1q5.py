# Write a program that takes a string input from the user and writes it to a text file.
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"The content has been successfully written to {filename}")
    except IOError:
        print("An error occurred while writing to the file.")

# Example usage
if __name__ == "__main__":
    user_input = input("Enter the text you want to write to the file: ")
    filename = "output.txt"  # You can change this to any filename you prefer
    write_to_file(filename, user_input)










