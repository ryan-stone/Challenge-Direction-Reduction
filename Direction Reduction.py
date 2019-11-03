def dir_reduc(stringlist):
    finished = False
    while not finished:
        finished = True
        for i in range(len(stringlist)-1):
            if stringlist[i] == "NORTH" and stringlist[i+1] == "SOUTH":
                finished = False
            elif stringlist[i] == "SOUTH" and stringlist[i+1] == "NORTH":
                finished = False
            elif stringlist[i] == "EAST" and stringlist[i+1] == "WEST":
                finished = False
            elif stringlist[i] == "WEST" and stringlist[i+1] == "EAST":
                finished = False
            if not finished:
                print("Removing " + stringlist[i] + " and " + stringlist[i+1] + " (" + str(i) + "," + str(i+1) + ")")
                stringlist = remove2(stringlist, i)
                print(stringlist)
                break
    return stringlist


def remove2(stringlist, pos):
    stringlist.pop(pos)
    stringlist.pop(pos)
    return stringlist


a = ["NORTH", "SOUTH", "NORTH", "WEST"]
print(a)
print(dir_reduc(a))
print("------------------------------------\n")

b = ["SOUTH", "WEST", "EAST", "NORTH", "WEST", "NORTH", "EAST", "WEST", "SOUTH", "NORTH"]
print(b)
print(dir_reduc(b))
print("------------------------------------\n")

c = ["WEST", "NORTH", "EAST", "SOUTH", "NORTH", "WEST", "SOUTH", "EAST"]
print(c)
print(dir_reduc(c))
print("------------------------------------\n")
