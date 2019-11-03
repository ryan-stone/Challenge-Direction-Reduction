# ---------------------------------------------------------------------------------------------
# Ryan Stone
# Direction Reduction Challenge
# 11/02/2019
# ---------------------------------------------------------------------------------------------
# BACKGROUND
#
# Once upon a time, on a way through the old wild west,va man was given directions to go from
# one point to another.

# The directions were "NORTH", "SOUTH", "WEST", "EAST".
# Clearly "NORTH" and "SOUTH" are  opposite, "WEST" and "EAST" too.
# Going to one direction and coming back the opposite  direction is a needless effort.
#
# Since this is the wild west, with dreadful weather and not much water, it's important
# to save yourself some energy, otherwise you might die of thirst!
# ---------------------------------------------------------------------------------------------
# TASK
# Write a function, Direction Reduction, which will take an array of strings and returns an
# array of strings with the needless directions removed (W<->E or S<->N side by side).
# ---------------------------------------------------------------------------------------------
# RULES and EXAMPLES
# In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and
# coming back right away. What a waste of time! Better to do nothing.

# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore,
# the final result is []
#
# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly
# opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the
# whole path is reducible to ["WEST", "WEST"].
# ---------------------------------------------------------------------------------------------


# The direction reduction function accepts a list of strings and reduces the list by removing
# adjacent conflicting strings until the list is no longer reducible.
# THe function returns the list of strings when the list is no longer reducible.
def direction_reduction(stringlist):
    reducible = True
    while reducible:
        reducible = False
        for i in range(len(stringlist)-1):
            if stringlist[i] == "NORTH" and stringlist[i+1] == "SOUTH":
                reducible = True
            elif stringlist[i] == "SOUTH" and stringlist[i+1] == "NORTH":
                reducible = True
            elif stringlist[i] == "EAST" and stringlist[i+1] == "WEST":
                reducible = True
            elif stringlist[i] == "WEST" and stringlist[i+1] == "EAST":
                reducible = True
            if reducible:
                print("Removing " + stringlist[i] + " and " + stringlist[i+1] + " (" + str(i) + "," + str(i+1) + ")")
                stringlist = remove2(stringlist, i)
                print(stringlist)
                break
    return stringlist


# Removes adjacent elements from the list.
# pos indicates the position of the first element.
# Returns the new list back to the calling statement.
def remove2(stringlist, pos):
    stringlist.pop(pos)
    stringlist.pop(pos)
    return stringlist


# Example Outputs
a = ["NORTH", "SOUTH", "NORTH", "WEST"]
print(a)
print(direction_reduction(a))
print("------------------------------------\n")

b = ["SOUTH", "WEST", "EAST", "NORTH", "WEST", "NORTH", "EAST", "WEST", "SOUTH", "NORTH"]
print(b)
print(direction_reduction(b))
print("------------------------------------\n")

c = ["WEST", "NORTH", "EAST", "SOUTH", "NORTH", "WEST", "SOUTH", "EAST"]
print(c)
print(direction_reduction(c))
print("------------------------------------\n")
