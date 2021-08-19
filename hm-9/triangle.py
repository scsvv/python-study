floors = 7

for row in range(1, floors + 1):
    for col in range(1, (floors*2)):
        if row == floors or row+col == floors + 1\
            or col - row == floors - 1:
            print("*", end="")
        else:
            print(end=" ")
    print()
print('\n\n')

for row in range(1, floors + 1):
    for col in range(1, (floors*2)):
        if row+col >= floors + 1 and col - row <= floors - 1:
            print("*", end="")
        else:
            print(end=" ")
    print()
print('\n\n')

for row in range(1, floors*2 + 1):
    for col in range(1, (floors*2)):
        if row == floors or col == floors\
        or row + col == floors + 1 or row - col == floors\
        or col - row == floors - 1:
            print("*", end="")
        else:
            print(end=" ")
    print()
print('\n\n')