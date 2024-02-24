import inflect
import re

def convert_numbers_to_text(file_name):
    try:
        # Initialize inflect engine
        p = inflect.engine()

        # Open the file for reading
        with open(file_name, 'r') as file:
            # Read the entire content of the file
            content = file.read()

        # Use regex to find all numbers in the content
        numbers = re.findall(r'\b\d+\b', content)

        # Replace each number with its textual representation
        for number in numbers:
            text_representation = p.number_to_words(number)
            content = content.replace(number, text_representation)

        # Write the modified content back to the file
        with open(file_name, 'w') as file:
            file.write(content)

        print("Numbers in the file '{}' have been converted to text successfully.".format(file_name))

    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
    except Exception as e:
        print("An error occurred:", str(e))

# Call the function with the file name
convert_numbers_to_text("file2.txt")
