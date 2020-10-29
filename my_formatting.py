import struct

my_float = 4435.9324
data = struct.pack("d", my_float)

print("decimal: ", [f"{i:d}" for i in data])
print("hex:     ", [f"{i:02x}" for i in data])
print("octal:   ", [f"{i:o}" for i in data])
print("binary:  ", [f"{i:08b}" for i in data])

print()

text = "my text"
print(f"{text:<30}") # aligned lef
print(f"{text:>30}") # aligned right
print(f"{text:^30}") # centered
print(f"{text:-^30}")  # centered with fill char

print()

print(f"{my_float:e}")
print(f"{my_float:.2f}")
