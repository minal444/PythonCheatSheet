# Path
from pathlib import Path

# Absolute Path
# c:\Program\Python

# this will refere current path
path = Path("ecommerce")
print(path.exists())

# path = Path("Email")
# print(path.mkdir())  # create directory
# print(path.rmdir())  # delete directory

# find all directory and files in the path
path = Path()
print(path.glob("*.py"))

# search for all the files in current dir
for file in path.glob("*"):
    print(file)

# Pypi for all different kind of library
# web scraping and crawler to extract information


