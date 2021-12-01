# I modified the data file to remove one blank character at the end
# This can also be done in code by just adding a [:-1] to the following line.
data = open("C:\input.txt","r").read().split("\n")

# Convert every entry in data into an int (it gets read as a string by default)
data = [int(i) for i in data]

counter = 0

prev = data[0]

for number in data:
    if(number > prev):
        counter += 1
    prev = number

print(counter)
