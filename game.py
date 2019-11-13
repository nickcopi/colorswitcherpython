import tkinter
import random


#C = tkinter.Canvas(top, bg="blue", height=250, width=300)
#C.pack()
#
#coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start=0, extent=150, fill="red")


class Game:
    SIZE = 500
    def __init__(self,top):
        self.top = top
        self.won = False
        self.initGrid()
        self.initCanvas()
        top.mainloop()

    def initGrid(self):
        size = Game.SIZE//Square.SIZE
        self.grid = [[Square(i,j) for i in range(size)] for j in range(size)]

    def initCanvas(self):
        self.canvas = tkinter.Canvas(self.top, bg='white', height=Game.SIZE, width=Game.SIZE)
        self.canvas.pack();
        self.canvas.after(17,self.render)
        self.canvas.bind('<Button-1>',self.handleClick)

    def render(self):
        self.canvas.delete('all')
        for x in range(len(self.grid)) :
                for y in range(len(self.grid[x])):
                    self.grid[x][y].render(self.canvas)
        if self.won:
            self.canvas.create_text(Game.SIZE//2,Game.SIZE//2,text='You win!',font=("Arial",40))
        self.canvas.after(17,self.render)
    def handleClick(self,event):
        if self.won:
            return
        x = event.x//Square.SIZE
        y = event.y//Square.SIZE
        self.doGridClick(y,x)
    def doGridClick(self,x,y):
        if x-1 >= 0:
            self.grid[x-1][y].toggleSet()
        if y-1 >= 0:
            self.grid[x][y-1].toggleSet()
        if x+1 < len(self.grid):
            self.grid[x+1][y].toggleSet()
        if y+1 < len(self.grid):
            self.grid[x][y+1].toggleSet()
        self.grid[x][y].toggleSet()
        self.checkWin()
    def checkWin(self):
        if(self.isWinState()):
            self.won = True
    def isWinState(self):
            allSet = True
            allUnset = True
            for x in range(len(self.grid)) :
                for y in range(len(self.grid[x])):
                    if self.grid[x][y].set:
                        allUnset = False
                    if not self.grid[x][y].set:
                        allSet = False
            return allSet or allUnset



            

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


