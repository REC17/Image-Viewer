# The MIT License
#
# Copyright (c) 2011 Wyss Institute at Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php
"""
compositeImage.py

Created by Roger Conturie 2011-07-12
"""

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
        self.livebrowser.setText(QString("X..." + str(x) + " Y..." + str(y) + " Pixel Value..." + str(self.rawimage[y, x])))
        
        for i in range(3):
            for j in range(3):
                pass
          # print self.rawimage[y + i-1, x + j-1].astype(numpy.uint8)
            
    
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


