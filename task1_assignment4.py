filename = 'sampe.txt'
try:
    file = open(filename, 'r')
    a = file.readlines()
    print("Reading file content:")
    print("Line 1:", a[0])
    print("Line 2:", a[1])
    file.close()
except FileNotFoundError:
    print("Error: The file", filename, "was not found")