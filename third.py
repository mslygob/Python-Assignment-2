def create_dictionary_from_file(file_name, delimiter=':'):
    try:
        # Initialize an empty dictionary
        result_dict = {}

        # Open the file for reading
        with open(file_name, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                # Split the line using the specified delimiter
                key, value = line.strip().split(delimiter, 1)
                
                # Assign key-value pair to the dictionary
                result_dict[key.strip()] = value.strip()

        print("Dictionary created successfully from the file '{}'.".format(file_name))
        return result_dict

    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
        return {}
    except Exception as e:
        print("An error occurred:", str(e))
        return {}

# Call the function with the file name
file3_dict = create_dictionary_from_file("file3.txt")

# Print the dictionary
print(file3_dict)
