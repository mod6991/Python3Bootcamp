file = open("story.txt") # open a file

print(file.read()) # print full file content
file.seek(0) # seeks beginning of the file

lines = file.readlines() # get an array with all file lines
print()
i = 0
for line in lines:
    print(f"line {i}: '{line}'")
    i += 1

file.close()

print()
if file.closed:
    print("file il closed")
else:
    print("file is not closed")

# ----------------
# 'with' statement
# ----------------

print()
with open("story.txt") as f:
    print(f.read())

if f.closed:
    print("file has been closed automatically with 'with' statement")
else:
    print("file is not closed")

# -------------
# Write to file
# -------------

with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")

