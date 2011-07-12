


class DistanceLine(QGraphicsItem):
    def __init__(self, mainWin, x1, y1, x2, y2):
        super(DistanceLine, self).__init__()
        self.mainWin = mainWin
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        self.stroke = QColor(255, 204, 153)
        self.rect = QRectF(0,0,100,100)


        if self.mainWin.lastline is not None:
            try:
                LLS = self.mainWin.lastline.scene()
                LLS.removeItem(self.mainWin.lastline)
            except:
                return
        self.mainWin.lastline = self

    def boundingRect(self):
        return self.rect
    
    def paint(self, painter, option, widget=None):
        painter.setPen(QPen(self.stroke))
        for i in range(9):
            x = (i+1)%3 -1
            y = (i+1)/3 -1
            line = QLine(self.x2 + x , self.y2 + y, self.x1 + x, self.y1 + y)
            painter.drawLine(line)
