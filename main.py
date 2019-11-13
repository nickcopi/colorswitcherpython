import tkinter
import random

top = tkinter.Tk()

#C = tkinter.Canvas(top, bg="blue", height=250, width=300)
#C.pack()
#
#coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start=0, extent=150, fill="red")


class Game:
    SIZE = 500
    def __init__(self):
        self.initGrid()
        self.initCanvas()
        top.mainloop()

    def initGrid(self):
        size = Game.SIZE//Square.SIZE
        self.grid = [[Square(i,j) for i in range(size)] for j in range(size)]

    def initCanvas(self):
        self.canvas = tkinter.Canvas(top, bg='white', height=Game.SIZE, width=Game.SIZE)
        self.canvas.pack();
        self.canvas.after(17,self.render)

    def render(self):
        self.canvas.delete('all')
        for x in range(len(self.grid)) :
                for y in range(len(self.grid[x])):
                    self.grid[x][y].render(self.canvas)
        self.canvas.after(17,self.render)

class Square:
    SIZE = 100
    SET_COLOR = 'red'
    UNSET_COLOR = 'blue'
    def __init__(self,x,y):
        self.x = x * Square.SIZE
        self.y = y * Square.SIZE
        if random.choice([1,2,3]) == 1:
            self.set = True
        else:
            self.set = False
    def render(self,canvas):
        if self.set:
            fillColor = Square.SET_COLOR
        else:
            fillColor = Square.UNSET_COLOR
        canvas.create_rectangle(self.x,self.y,self.x+Square.SIZE,self.y+Square.SIZE,fill = fillColor,width=0)
    def toggleSet(self):
        self.set = not self.set

game = Game()

