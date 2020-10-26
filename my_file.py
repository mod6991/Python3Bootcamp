def write_bytearray_to_file(barr, path):
    with open(path, "wb") as file:
        file.write(barr)

text = input("Enter text: ")

ba_iso = bytearray(text, "iso-8859-1")
print(f"iso-8859-1: {ba_iso}")
write_bytearray_to_file(ba_iso, "file_iso.txt")

ba_utf8 = bytearray(text, "utf-8")
print(f"utf-8: {ba_utf8}")
write_bytearray_to_file(ba_utf8, "file_utf8.txt")

ba_cp1252 = bytearray(text, "cp1252")
print(f"cp1252: {ba_cp1252}")
write_bytearray_to_file(ba_cp1252, "file_cp1252.txt")

