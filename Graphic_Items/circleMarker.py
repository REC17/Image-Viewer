import os, sys, math, numpy #,png, itertools
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class CircleMarker(QGraphicsItem):
    def __init__(self, compImage, mainWin, controller, position, futureparent):
        super(CircleMarker, self).__init__()
        self.compImage = compImage
        self.mainWin = mainWin
        self.controller = controller
        self.futureparent = futureparent
        self.fill = QColor(100, 204, 150)
        self.stroke = QColor(153, 204, 255)
        self.setPos(position)
        self.mainWin.ClearDots.setEnabled(True)

        if len(self.controller.lastcircle) > 0:
            DL = DistanceLine(self.mainWin, self.controller, self.controller.lastcircle[0], self.controller.lastcircle[1], position.x(), position.y())
            DL.setParentItem(self.futureparent)        
        
        self.futureparent.update()
        self.controller.lastcircle = []
        self.controller.lastcircle.append(position.x())
        self.controller.lastcircle.append(position.y())
        
    def boundingRect(self):
        return QRectF(-6,-6,12,12)
    
    def paint(self, painter, option, widget=None):
    #    painter.setBrush(QBrush(self.fill))
        painter.setPen(QPen(self.stroke))
        painter.drawEllipse(QRectF(-5, -5, 10, 10))
        painter.drawEllipse(QRectF(-6,-6,12,12))

class DistanceLine(QGraphicsItem):
    def __init__(self, mainWin, controller, x1, y1, x2, y2):
        super(DistanceLine, self).__init__()
        self.mainWin = mainWin
        self.controller = controller
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.stroke = QColor(255, 204, 153)
        self.rect = QRectF(0,0,100,100)

        if self.controller.lastline is not None:
            try:
                LLS = self.controller.lastline.scene()
                LLS.removeItem(self.controller.lastline)
            except:
                return
        self.controller.lastline = self

    def boundingRect(self):
        return self.rect
    
    def paint(self, painter, option, widget=None):
        painter.setPen(QPen(self.stroke))
        for i in range(9):
            x = (i+1)%3 -1
            y = (i+1)/3 -1
            line = QLine(self.x2 + x , self.y2 + y, self.x1 + x, self.y1 + y)
            painter.drawLine(line)
