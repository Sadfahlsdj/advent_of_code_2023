# Python3 implementation of the approach

# Function that returns true if
# the given pixel is valid

# COMPLETELY copied from https://www.geeksforgeeks.org/flood-fill-algorithm/
def isValid(screen, m, n, x, y, prevC, newC):
    if x < 0 or x >= m \
            or y < 0 or y >= n or \
            screen[x][y] != prevC \
            or screen[x][y] == newC:
        return False
    return True


# FloodFill function
def floodFill(screen,
              m, n, x,
              y, prevC, newC, counter):
    queue = []

    # Append the position of starting
    # pixel of the component
    queue.append([x, y])

    # Color the pixel with the new color
    screen[x][y] = newC

    # While the queue is not empty i.e. the
    # whole component having prevC color
    # is not colored with newC color
    while queue:

        # Dequeue the front node
        currPixel = queue.pop()

        posX = currPixel[0]
        posY = currPixel[1]

        # Check if the adjacent
        # pixels are valid
        if isValid(screen, m, n,
                   posX + 1, posY,
                   prevC, newC):
            # Color with newC
            # if valid and enqueue
            screen[posX + 1][posY] = newC
            queue.append([posX + 1, posY])
            # only counts if the tile being moved to is the "center" of a 3x3 square
            if (posX + 1) % 3 == 1 and posY % 3 == 1:
                counter += 1

        if isValid(screen, m, n,
                   posX - 1, posY,
                   prevC, newC):
            screen[posX - 1][posY] = newC
            queue.append([posX - 1, posY])
            if (posX - 1) % 3 == 1 and posY % 3 == 1:
                counter += 1

        if isValid(screen, m, n,
                   posX, posY + 1,
                   prevC, newC):
            screen[posX][posY + 1] = newC
            queue.append([posX, posY + 1])
            if posX % 3 == 1 and (posY + 1) % 3 == 1:
                counter += 1

        if isValid(screen, m, n,
                   posX, posY - 1,
                   prevC, newC):
            screen[posX][posY - 1] = newC
            queue.append([posX, posY - 1])
            if posX % 3 == 1 and (posY - 1) % 3 == 1:
                counter += 1
    return counter