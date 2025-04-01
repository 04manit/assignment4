text = input("Enter text to write to the file: ")
file = open('output.txt', 'w')
file.write(text)
print("Data successfully written to output.txt\n")
file.close()


text2 = input("Enter additional text to append: ")
file2 = open('output.txt', 'a')
file2.write("\n" + text2)
print("Data successfully appended.\n")
file2.close()

file3 = open('output.txt', 'r')
print("Final content of output.txt is :")
print(file3.read())
file3.close()