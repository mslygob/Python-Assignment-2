def reverse_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        lines.reverse()

        with open(file_name, 'w') as file:
            file.writelines(lines)
        
        print("Contents of the file '{}' have been reversed successfully.".format(file_name))
    
    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
    except Exception as e:
        print("An error occurred:", str(e))

reverse_file_contents("file1.txt")
