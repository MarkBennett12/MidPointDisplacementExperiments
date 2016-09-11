from tkinter import *
import random

# recursive midpoint displacement algorithm with no adaptions
def standardMidPointDisplacement(points, lineStart, lineEnd, maxVerticalOffset, iterations, displaceRand):
    if iterations == 0:
        points.append(lineEnd)
        return

    lineLength = lineEnd[0] - lineStart[0]
    lineMidpoint = lineLength / 2

    newHeight = ((lineStart[1] + lineEnd[1]) / 2) - displaceRand.randint(-maxVerticalOffset, maxVerticalOffset)
    midpoint = (lineStart[0] + lineMidpoint, newHeight)

    # Displace each half of the line
    standardMidPointDisplacement(points, lineStart, midpoint, maxVerticalOffset // 2, iterations - 1, displaceRand)
    standardMidPointDisplacement(points, midpoint, lineEnd, maxVerticalOffset // 2, iterations - 1, displaceRand)

# recursive midpoint displacement algorithm with a random 'midpoint' position
def MPDVariableMidPoint(points, lineStart, lineEnd, maxVerticalOffset, iterations, displaceRand, midpointRand):
    if iterations == 0:
        points.append(lineEnd)
        return

    lineLength = lineEnd[0] - lineStart[0]
    # set the midpoint to a random point between line start and line end
    lineMidpoint = midpointRand.randint(0, lineLength)

    newHeight = ((lineStart[1] + lineEnd[1]) / 2) - displaceRand.randint(-maxVerticalOffset, maxVerticalOffset)
    midpoint = (lineStart[0] + lineMidpoint, newHeight)

    # Displace each half of the line
    MPDVariableMidPoint(points, lineStart, midpoint, maxVerticalOffset // 2, iterations - 1, displaceRand, midpointRand)
    MPDVariableMidPoint(points, midpoint, lineEnd, maxVerticalOffset // 2, iterations - 1, displaceRand, midpointRand)

# recursive midpoint displacement algorithm with variable lacunarity
def MPDVariableLacunarity(points, lineStart, lineEnd, maxVerticalOffset, iterations, displaceRand, lacunarityRand):
    if iterations == 0:
        points.append(lineEnd)
        return

    lineLength = lineEnd[0] - lineStart[0]
    lineMidpoint = lineLength / 2

    # default to having no displacement
    newHeight = (lineStart[1] + lineEnd[1]) / 2
    # 50/50 chance of lacunarity
    if lacunarityRand.randint(0, 100) < 50:
        newHeight -= displaceRand.randint(-maxVerticalOffset, maxVerticalOffset)
    midpoint = (lineStart[0] + lineMidpoint, newHeight)

    # Displace each half of the line
    MPDVariableLacunarity(points, lineStart, midpoint, maxVerticalOffset // 2, iterations - 1, displaceRand, lacunarityRand)
    MPDVariableLacunarity(points, midpoint, lineEnd, maxVerticalOffset // 2, iterations - 1, displaceRand, lacunarityRand)

# recursive midpoint displacement algorithm with variable lacunarity and random midpoint
def MPDVariableLacunarityAndMidPoint(points, lineStart, lineEnd, maxVerticalOffset, iterations, displaceRand, midpointRand, lacunarityRand):
    if iterations == 0:
        points.append(lineEnd)
        return

    lineLength = lineEnd[0] - lineStart[0]
    lineMidpoint = midpointRand.randint(0, lineLength)

    # default to having no displacement
    newHeight = (lineStart[1] + lineEnd[1]) / 2
    # 50/50 chance of lacunarity
    if lacunarityRand.randint(0, 100) < 50:
        newHeight -= displaceRand.randint(-maxVerticalOffset, maxVerticalOffset)
    midpoint = (lineStart[0] + lineMidpoint, newHeight)

    # Displace each half of the line
    MPDVariableLacunarityAndMidPoint(points, lineStart, midpoint, maxVerticalOffset // 2, iterations - 1, displaceRand, midpointRand, lacunarityRand)
    MPDVariableLacunarityAndMidPoint(points, midpoint, lineEnd, maxVerticalOffset // 2, iterations - 1, displaceRand, midpointRand, lacunarityRand)

# recursive midpoint displacement algorithm with a random 'midpoint' position
def MPDVariableMidPointTrianglularRand(points, lineStart, lineEnd, maxVerticalOffset, iterations, displaceRand, midpointRand):
    if iterations == 0:
        points.append(lineEnd)
        return

    lineLength = lineEnd[0] - lineStart[0]
    # set the midpoint to a random point between line start and line end
    lineMidpoint = int(midpointRand.triangular(0, lineLength, lineLength / 2))

    newHeight = ((lineStart[1] + lineEnd[1]) / 2) - displaceRand.randint(-maxVerticalOffset, maxVerticalOffset)
    midpoint = (lineStart[0] + lineMidpoint, newHeight)

    # Displace each half of the line
    MPDVariableMidPointTrianglularRand(points, lineStart, midpoint, maxVerticalOffset // 2, iterations - 1, displaceRand, midpointRand)
    MPDVariableMidPointTrianglularRand(points, midpoint, lineEnd, maxVerticalOffset // 2, iterations - 1, displaceRand, midpointRand)



# set up the window and canvas for drawing and pass in the line (terrain) to draw
def display(canvasWidth, canvasHeight, line):
    window = Tk()

    canvas = Canvas(window, 
               width=canvasWidth,
               height=canvasHeight)
    canvas.pack()

    # draw our terrain here
    for i in range(len(line) - 1):
        #print(str(i))
        canvas.create_line(line[i][0], line[i][1], line[i + 1][0], line[i + 1][1])

    mainloop()

# set up the line and create the terrain and draw it
def run(dSeed, mSeed, lSeed, selection, roughness, iterations):
    # window size
    width = 800
    height = 600

    displaceRand = random.Random()
    displaceRand.seed(dSeed)
    midPointRand = random.Random()
    midPointRand.seed(mSeed)
    lacunarityRand = random.Random()
    lacunarityRand.seed(lSeed)

    # ensures the line does not start or end at the edges of the window to aid visibility
    lineXOffset = 50

    # put the line halfway up the window
    lineYPosition = height // 2

    # get the start and end points of the x coordinate
    lineStartX = lineXOffset
    lineEndX = width - lineXOffset

    # the maximum amount of vertical displcement for the midpoint displacement algorithm
    verticalOffset = 200

    # the first point needs to be in the list
    linePoints = [(lineStartX, lineYPosition)]

    if selection == 1:
        standardMidPointDisplacement(linePoints, linePoints[0], (lineEndX, lineYPosition), roughness, iterations, displaceRand)
    elif selection == 2:
        MPDVariableMidPoint(linePoints, linePoints[0], (lineEndX, lineYPosition), roughness, iterations, displaceRand, midPointRand)
    elif selection == 3:
        MPDVariableLacunarity(linePoints, linePoints[0], (lineEndX, lineYPosition), roughness, iterations, displaceRand, lacunarityRand)
    elif selection == 4:
        MPDVariableLacunarityAndMidPoint(linePoints, linePoints[0], (lineEndX, lineYPosition), roughness, iterations, displaceRand, midPointRand, lacunarityRand)
    elif selection == 5:
        MPDVariableMidPointTrianglularRand(linePoints, linePoints[0], (lineEndX, lineYPosition), roughness, iterations, displaceRand, midPointRand)
    else:
        print("invalid selection")
    print(str(linePoints))
    display(width, height, linePoints)

run(34567, 12345, 67890, 5, 100, 8)