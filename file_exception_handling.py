# Create a program that reads a file and writes a modified version to a new file.
try:
    # Open the input file in read mode
    with open('input.txt', 'r') as infile:
        # Read the contents of the file
        data = infile.read()
    
    # Modify the data (for example, convert to uppercase)
    modified_data = data.upper()
    
    # Open the output file in write mode
    with open('output.txt', 'w') as outfile:
        # Write the modified data to the new file
        outfile.write(modified_data)
    print("File has been modified and saved as output.txt")

except FileNotFoundError:
    print("Error: The input file was not found.")

# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    filename = input("Enter the filename to read: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(f"File content: {content}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")