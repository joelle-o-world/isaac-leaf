# The basics for drawing lines from a set of coordinates
import tkinter
from tkinter import Canvas


class Line:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    
    def __str__(self):
        return "({}, {}) -> ({}, {})".format(self.x0, self.y0, self.x1, self.y1)



def drawGeometry(lines):
    window = tkinter.Tk()
    width = 500
    height = 500
    window.geometry("{}x{}".format(width, height))
    canvas = Canvas(window, width=width, height=height)
    canvas.pack()
    for line in lines:
        # print("Plotting: ", line)
        canvas.create_line(line.x0, line.y0, line.x1, line.y1)
    window.mainloop()


# Example usage:
# drawGeometry([Line(0,0, 100, 100), Line(200, 10, 0, 0)])

from math import pi, cos, sin, sqrt, pow
def doSomeTrigonometryWoopWoop(x, y, angle, distance):
    return { "x": distance * cos(angle/360.0 * 2 * pi) + x, "y": distance * sin(angle /360.0* 2 * pi) + y }

# Here is where the fun starts
class LittleMan:
    def __init__(self, x, y, angle, intention="basic"):
        self.x = x
        self.y = y
        self.angle = angle
        self.intention = intention
        self.isInTheMood = True
        self.generation = 1

    def chuckAnotherLittleManAheadOfYourself(self, distance):
        point = doSomeTrigonometryWoopWoop(self.x, self.y, self.angle, distance)
        # print(point)
        freshlyChuckedMan = LittleMan(point["x"], point["y"], self.angle, self.intention)
        freshlyChuckedMan.generation = self.generation + 1
        return freshlyChuckedMan

    def getDistance(self, someOtherLittleMan):
        return sqrt(pow(self.x - someOtherLittleMan.x, 2) + pow(self.y - someOtherLittleMan.y, 2))

    def proximityToNearestHeterosexual(self, otherHeterosexualMen):
        maxDistance = -1
        for justABro in otherHeterosexualMen:
            if justABro == self:
                continue
            distance = self.getDistance(justABro)
            if maxDistance == -1 or distance < maxDistance:
                maxDistance = distance
        return maxDistance











def generateALeaf(extensionRule, theMen = [LittleMan(250, 250, 0, "basic")]):
    lines = []

    def addGeneration():
        nextGeneration: list[LittleMan] = []
        for ourLittleMan in theMen:
            if ourLittleMan.isInTheMood:
                hisFreshlyChuckedLittleMen = extensionRule(ourLittleMan, theMen + nextGeneration)
                for newManOnTheScene in hisFreshlyChuckedLittleMen:
                    lines.append(Line(ourLittleMan.x, ourLittleMan.y, newManOnTheScene.x, newManOnTheScene.y))
                nextGeneration += hisFreshlyChuckedLittleMen
        return theMen +  nextGeneration

    for i in range(20):
        theMen = addGeneration()

    return lines



