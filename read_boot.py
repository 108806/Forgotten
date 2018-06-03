# read_boot_sector.py - Inspect the first 512 bytes of a file

import sys

in_file = open(sys.argv[1], 'rb')  # Provide a path to disk or ISO image
chunk_size = 512
data = in_file.read(chunk_size)
print(data)