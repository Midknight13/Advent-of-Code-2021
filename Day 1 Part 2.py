# I modified the data file to remove one blank character at the end
# This can also be done in code by just adding a [:-1] to the following line.
data = open("C:\input.txt","r").read().split("\n")

# Convert every element in data into an int, from a string
data = [int(i) for i in data]

counter = 0

for i in range(len(data)-3):
    if(data[i+3] > data[i]):
        counter += 1

print(counter)
