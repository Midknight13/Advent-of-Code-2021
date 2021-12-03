commandlist = open("C:\input.txt","r")

x = 0
y = 0

for command in commandlist:
    direction,distance = command.split(" ")
    distance = int(distance)
    if(direction == "forward"):
        x += distance
    else:
        y += ((direction == "down") - (direction == "up")) * distance

print(x*y)
