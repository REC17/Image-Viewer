from PyQt4.QtCore import *
from PyQt4.QtGui import *

class RectangleSection(QGraphicsItem):
    def __init__(self, position):
        super(RectangleSection, self).__init__()
        self.position = position
        self.fill = QColor(100, 204, 150)
        self.stroke = QColor(153, 204, 255)
        self.setPos(self.position)
        self.width = 1
        self.height = 1
        
    def boundingRect(self):
        return QRectF(0,0,0,0)
    
    def paint(self, painter, option, widget=None):
    #    painter.setBrush(QBrush(self.fill))
        painter.setPen(QPen(self.stroke))
      #  painter.drawRect(QRectF(-5, -5, 10, 10))
        painter.drawRect(QRectF(0,0,self.width,self.height))
