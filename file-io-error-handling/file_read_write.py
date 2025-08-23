# Open the input file (example: input.txt) and read its content
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (example: convert to uppercase)
modified_content = content.upper()

# Write modified content to a new file (output.txt)
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been modified and saved as output.txt")
