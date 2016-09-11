from tkinter import Tk, Canvas, Frame, BOTH
import MidpointDisplacement
import modifierFunctions

class gui(Frame):
    """interface for midpoint displacement tests"""
    def __init__(self, parent, w, h):
        Frame.__init__(self, parent)
        self.parent = parent
        self.width = w
        self.height = h

        self.parent.title("Midpoint Displacement Experiment")        
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self, width=self.width, height=self.height)        
        self.canvas.pack(fill=BOTH, expand=1)

        # Setup the random number generators with fixed seeds so the only factor changing the result
        # is the modifier function
        self.generator = MidpointDisplacement.MidpointDisplacement()
        self.generator.displaceRand.seed(1234)
        self.generator.iterations = 8

        # RNG modifier function
        self.generator.modifierFunction = modifierFunctions.karst

    def draw(self):
        # put the line halfway up the window
        lineYPosition = self.height // 2

        # get the start and end points of the x coordinate
        lineXOffset = 50
        lineStartX = lineXOffset
        lineEndX = self.width - lineXOffset

        line = self.generator.Generate((lineStartX, lineYPosition), (lineEndX, lineYPosition))

        # draw our terrain here
        for i in range(len(line) - 1):
            #print(str(i))
            self.canvas.create_line(line[i][0], line[i][1], line[i + 1][0], line[i + 1][1])

def main():
  
    window = Tk()
    interface = gui(window, 800, 600)
    #window.geometry("400x250+300+300")
    interface.draw()
    window.mainloop()  

main()
