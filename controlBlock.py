class ControlBlock:
    def __init__(self, title="visualiser", colors=("gray", "orange"),pos=(300,400),size=(120,40)):
        self.canvas = None
        self.entryVal = None
        self.fontSize = 12
        self.title = title
        self.freeFill = colors[0]
        self.dataFill = colors[1]
        self.operation = ""
        self.bWidth, self.bHeight = size
        self.bx, self.by = pos
        self.tagStr = "store"
