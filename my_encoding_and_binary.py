def write_file(path, text, encoding):
    with open(path, "w", encoding=encoding) as file:
        file.write(text)

def read_file(path, encoding):
    with open(path, "r", encoding=encoding) as file:
        return file.read()

text = input("Enter text: ")

# Write and read files with encoding

write_file("file_iso.txt", text, "iso-8859-1")
write_file("file_utf8.txt", text, "utf-8")
write_file("file_cp1252.txt", text, "cp1252")

print(read_file("file_iso.txt", "iso-8859-1"))
print(read_file("file_utf8.txt", "utf-8"))
print(read_file("file_cp1252.txt", "cp1252"))

# str to bytearray

ba_iso = bytearray(text, "iso-8859-1")
print(f"iso-8859-1: {ba_iso}")
ba_utf8 = bytearray(text, "utf-8")
print(f"utf-8: {ba_utf8}")
ba_cp1252 = bytearray(text, "cp1252")
print(f"cp1252: {ba_cp1252}")

# bytearray to str

str_iso = ba_iso.decode(encoding="iso-8859-1")
str_utf8 = ba_utf8.decode(encoding="utf-8")
str_cp1252 = ba_cp1252.decode(encoding="cp1252")

import struct

my_int = 1024
my_float = 5.998

binary_int = struct.pack('>i', my_int)
print(binary_int)
print([hex(i) for i in binary_int])
binary_float = struct.pack('d', my_float)
print(binary_float)
print([hex(i) for i in binary_float])