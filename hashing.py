import sys
import hashlib

chunk_size = 2048 # Edit here to change amount of bytes it reads into memory at once

path = ""
counter = 0

md5 = hashlib.md5()
sha1 = hashlib.sha1()

if len(sys.argv) > 1: # Check if path was given as argument
    path = sys.argv[1] 
else:
    path = input("File: ") # If not ask for path to file

try:
    file = open(path, 'rb') # Open given file
except IOException: # Error handling for file opening
    print("Problem opening the file. Please make sure the path is written correctly.")
    print("Closing application. Please restart to try again.")
    sys.exit()

try:
    for buffer in file:
        part = file.read(chunk_size) # Read file in chunks
        counter = counter + 1 # Count how many chunks the file gets split into
        if not part: # If there is nothing left to read break from the loop
          	break
        # Update the current hashes
        md5.update(part)
        sha1.update(part)
    file.close()
except Exception: # Exception handling in case there is a problem hashing the file content (or reading it)
    print("Problem hashing file content.") 
    print("Closing application. Please restart to try again.")
    sys.exit()   

# Tell user how many chunks the file was split into
print("Hashing " + str(counter) + " chunk(s) of max. " + str(chunk_size) + " bytes each...")

md5_hash = md5.hexdigest()
sha1_hash = sha1.hexdigest()

# Display hashes
print("MD5: " + md5_hash)
print("SHA1: " + sha1_hash)
