f = open("demofile.txt", "w")
x = input('enter text ')
f.write(x)
f.close()

# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
