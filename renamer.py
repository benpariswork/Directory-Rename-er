import os

def rename_files():
    directory = input("Enter the directory path: ")
    prefix = input("Enter the prefix: ")
    i = 1
    for filename in os.listdir(directory):
        if filename not in [".DS_Store", ".", ".."]:
            # construct the full filepath by joining the directory path and filename
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                # Extract file extension
                file_ext = os.path.splitext(file_path)[1]
                # check if the file is of the specified format
                if file_ext in ['.jpg', '.png', '.mp4']:
                    # Construct new file name
                    new_name = prefix + str(i) + file_ext
                    # Construct new file path
                    new_path = os.path.join(directory, new_name)
                    # Rename the file
                    os.rename(file_path, new_path)
                    i += 1
    print("files have been renamed successfully.")

# call the function
rename_files()

