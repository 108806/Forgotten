# Cast bytes to bytearray
mutable_bytes = bytearray(b'\x00\x0F')

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
print(mutable_bytes)

# Cast bytearray back to bytes
immutable_bytes = bytes(mutable_bytes)
print(immutable_bytes)


"""
To create a mutable object you need to use the bytearray type. With a bytearray you can do everything you can with other mutables like push, pop, insert, append, delete, and sort.
"""