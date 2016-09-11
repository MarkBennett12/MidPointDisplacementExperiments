import random
import math

#######################################################################################
# Stores the data for the midpoint displacement algorithm
#######################################################################################
class MidpointDisplacement(object):
    """experiment with the midpoint displacement algorithm"""
    def __init__(self):
        self.displaceRand = random.Random()
        self.midPointRand = random.Random()
        self.lacunarityRand = random.Random()

        self.points = []
        self.maxVerticalOffset = 100
        self.lacunarityScale = 0
        self.iterations = 0
        self.modifierFunction = None

    #######################################################################################
    # Calculates a modifier to the random displacement in order to allow for variable
    # height displacements.
    #######################################################################################
    def GetCalculatedDisplacementModifier(self, value, maxValue):
        print("interation = " + str(value))
        range = self.modifierFunction(value)
        print("f(x) = " + str(range))
        # Normalise the result to try to keep it within 0 to 1 as much as possible
        modifier = range / maxValue
        # clamp the result to a range between 0 and 1
        if modifier < 0.0:
            return 0.0
        return modifier

    #######################################################################################
    # recursive midpoint displacement algorithm with no adaptions
    #######################################################################################
    def MidPointDisplacement(self, lineStart, lineEnd, verticalOffset, iteration):
        if iteration == 0:
            self.points.append(lineEnd)
            return

        lineLength = lineEnd[0] - lineStart[0]
        lineMidpoint = lineLength / 2

        # Invert the current iteration value so it ascends from 0 to max iterations for the displacement modifier
        incrementedIteration = self.iterations - iteration + 1
        # Displace the midpoint by a random amount modified by the modifier function
        modifier = self.GetCalculatedDisplacementModifier(incrementedIteration, self.iterations)
        print("normalised = " + str(modifier))
        newHeight = ((lineStart[1] + lineEnd[1]) / 2) - (self.displaceRand.randint(-verticalOffset, verticalOffset) * modifier)
        midpoint = (lineStart[0] + lineMidpoint, newHeight)

        # Displace each half of the line
        self.MidPointDisplacement(lineStart, midpoint, verticalOffset // 2, iteration - 1)
        self.MidPointDisplacement(midpoint, lineEnd, verticalOffset // 2, iteration - 1)

    #######################################################################################
    # Call the midpoint displacement fmethod with appropriate arguments
    #######################################################################################
    def Generate(self, lineStart, lineEnd):
        self.points = [lineStart]
        self.MidPointDisplacement(lineStart, lineEnd, self.maxVerticalOffset, self.iterations)
        #self.MPDVariableLacunarityAndMidPoint(lineStart, lineEnd, self.iterations, self.scale, self.lacunarityScale)
        return self.points