import os
import time
import tempfile

# Print current dir
curDIr = os.getcwd()
print(curDIr)

# Create a directory

os.mkdir('Directory_Test')  # check in windows explorer

# After 5 sec rename the directory
time.sleep(5)
os.rename('Directory_Test', 'New_Directory_Test')

time.sleep(5)
os.rmdir('New_Directory_Test')



# Temporary file

print("Current temp directory: ", tempfile.gettempdir())
fp = tempfile.TemporaryFile()
fp.write(b'Hello World!')
fp.seek(0)
print(fp.read())
fp.close()
