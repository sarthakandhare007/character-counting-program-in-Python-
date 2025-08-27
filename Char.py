# Character counting from user input
text = input("Enter text: ")

count = 0
for ch in text:
    count += 1

print("Total characters entered:", count)
