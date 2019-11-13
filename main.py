import tkinter
top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)
C.pack()

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

top.mainloop()

class Game:
    SIZE = 500
    canvas
    ctx
    grid
    interval
    def __init__(self):
        initGrid(self)
    def initGrid(self):
        print ("hi")
    def initCanvas(self):
        self.canvas = tkinter.Canvas(top, bg="blue", height=250, width=300)
        self.canvas.pack();
        coord = 10, 50, 240, 210
        arc = self.canvas..create_arc(coord, start=0, extent=150, fill="red")

game = Game()

