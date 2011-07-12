import os, sys, math, numpy #,png, itertools
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Graphic_Items.circleMarker import CircleMarker

class CompImage(QGraphicsItem):
    def __init__(self, mainWin, compController, target, Image, source, selectedbrowser, livebrowser, searchbrowser, image_8bit, parent=None):
        super(CompImage, self).__init__(parent)
        self.target = target
        self.mainWin = mainWin
        self.compC = compController
        self.Image = Image
        self.source = source
        self.searchbrowser = searchbrowser
        self.rawimage = image_8bit
        self.selectedbrowser = selectedbrowser
        self.livebrowser = livebrowser
        self.setAcceptHoverEvents(True)


    def hoverEnterEvent(self, event):
        self.setCursor(QCursor(Qt.CrossCursor))
        
    def hoverMoveEvent(self, event):
        x = int(event.pos().x())
        y = int(event.pos().y())
        pixloc = x + y*1000
        self.livebrowser.setText(QString("X..." + str(x) + "    Y..." + str(y) + "    Pixel Value..." + str(self.rawimage[y, x])))
        
        for i in range(3):
            for j in range(3):
                pass
          #      print self.rawimage[y + i-1, x + j-1].astype(numpy.uint8)
            
    
    def searchExecuted(self, x, y):
        self.searchbrowser.setText(QString("Pixel Value..." + str(self.rawimage[y, x])))
        
    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()      
        self.selectedbrowser.append(QString(str(x) + "\t" + str(y) + "\t" + str(self.rawimage[y, x])))

        if self.compC.dotpermission == True:
            cm = CircleMarker(self, self.mainWin, self.compC, QPointF(x, y), self)
            cm.setParentItem(self)
        
    def boundingRect(self):
        return self.source

    def paint(self, painter, option, widget=None):
        painter.drawImage(self.target, self.Image, self.source)
        painter.drawRect(self.target)

