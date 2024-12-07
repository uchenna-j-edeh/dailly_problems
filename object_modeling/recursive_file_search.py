"""
Given a file path. Look through all the files in the path recurvice. for each file open, it for
reading. Scan through the line for a line that ends in a give character. character wii be provided via ags
"""

import os

def find_str_in_files(file_path, str_to_find):
  """
  This function recursively searches for a string in all files within a given directory.

  Args:
    file_path: The path to the directory to search.
    str_to_find: The string to search for.

  Returns:
    A list of file paths where the string was found.
  """
  found_files = []
  for root, _, files in os.walk(file_path):
    for file in files:
      full_path = os.path.join(root, file)
      if not full_path.endswith(".py"):
        # print(f"")
        continue
      with open(full_path, 'r') as f:
        my_dict = {full_path: []}
        for line in f:
            if str_to_find in line:
                my_dict[full_path].append(line)
        # file_content = f.read()
        # if str_to_find in file_content:
        #   found_files.append(full_path)
        found_files.append(my_dict)
  return found_files

# Example usage
file_path = "/Users/uchennaedeh/src/asapui/"
str_to_find = ";"
found_files = find_str_in_files(file_path, str_to_find)

if found_files:
  print(f"Found the string '{str_to_find}' in the following files:")
  for file in found_files:
    print(f"- {file}")
else:
  print(f"The string '{str_to_find}' was not found in any files.")