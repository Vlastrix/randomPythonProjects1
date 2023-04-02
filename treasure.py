
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


horizontal = int(position[0])
vertical =  int(position[1])
print("-----------------------------------------")
print(maps)
print("-----------------------------------------")

selected_row = maps[vertical - 1]
selected_row[horizontal - 1] = "X"
# map[vertical - 1][horizontal - 1] = "X" you can do it like on top or like this.

print(f"{row1}{row2}{row3}")
print("--------------------------------------------------------")
print(f"{row1}\n{row2}\n{row3}")