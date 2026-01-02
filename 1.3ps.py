import os

# You can change this to any directory you want
directory_path = "/"

# Get list of contents
contents = os.listdir(directory_path)

# Print each item
for item in contents:
    print(item)
