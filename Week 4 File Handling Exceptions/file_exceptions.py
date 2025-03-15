def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the filename to read: ")

        # Open the input file for reading
        with open(input_filename, "r") as infile:
            content = infile.read()
        
        # Modify the content (for example, make all text uppercase)
        modified_content = content.upper()

        # Create a new filename for the modified content
        output_filename = f"modified_{input_filename}"

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"File has been modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
