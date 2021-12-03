commandlist = open("C:\input.txt","r")

x = 0
y = 0
aim = 0

for command in commandlist:
    direction,distance = command.split(" ")
    distance = int(distance)
    if(direction == "forward"):
        x += distance
        y += aim * distance
    else:
        aim += ((direction == "down") - (direction == "up")) * distance

print(x*y)
