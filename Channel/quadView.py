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
quadView.py

Created by Roger Conturie 2011-07-12
"""

import os, sys, math, numpy #,png, itertools
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class QuadView(QGraphicsItem):
    def __init__(self, controller, image, zero, alpha, view, channel, selectedbrowser, livebrowser):
        super(QuadView, self).__init__(parent = None)
        self.image = image
        self.channel = channel
        self.zero = zero
        self.alpha = alpha
        self.view = view
        self.livebrowser = livebrowser
        self.selectedbrowser = selectedbrowser
        self.rect = QRectF(0, 0, 1000, 1000)
        self.controller = controller
        self.COL = self.controller.compinstanceL
        self.COL.append(self)
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        self.setCursor(QCursor(Qt.CrossCursor))

    def hoverMoveEvent(self, event):
        
        x = int(event.pos().x())
        y = int(event.pos().y())
        pixloc = x + y*1000
        self.livebrowser.setText(QString("X..." + str(x) + "    Y..." + str(y) + "    Pixel Value..." + str(self.image[y, x])))
        
        
    def mousePressEvent(self, event):
        
        x = event.pos().x()
        y = event.pos().y()

        if self.controller.enableQuadMag == True:   
            for i in self.COL:
                i.matrixresize(x, y)
        self.selectedbrowser.append(QString(str(x) + "\t" + str(y) + "\t" + str(self.image[y, x])))
        
    def matrixresize(self, x, y):
        matrix = self.view.matrix()
        scale = 2.0        
        if matrix.m11() == 256:
            self.view.resetMatrix()
            scale = 0.5**9
        if self.controller.zoom == "-":
            if matrix.m11() == 0.5:
                scale = 1
            else:
                scale = 0.5
        matrix.scale(scale, scale)
        self.view.setMatrix(matrix)
        self.view.centerOn(x, y)
     #   limit = 256/matrix.m11()
      #  log = math.log(limit, 2)
       # adjustlim = 1000/(2**(9-log))
        #self.view.ensureVisible(x, y, adjustlim, adjustlim)

    def searchExecuted(self, x, y):
        self.channel.setText(QString(str(self.image[y, x]))) 

 #       self.searchbrowser.setText(QString("Pixel Value..." + str(self.image[y, x])))
    
    def boundingRect(self):
        return self.rect

    def paint(self, painter, option, widget=None):
      #  painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
       # painter.fillRect(self.rect, Qt.transparent)
        image_ARGB_3D1 = numpy.dstack([self.image.astype(numpy.uint8), self.image.astype(numpy.uint8), self.image.astype(numpy.uint8), self.alpha])
        image_ARGB_2D1 = numpy.reshape(image_ARGB_3D1,(-1, 1000*4))
        Image1 = QImage(image_ARGB_2D1.data, 1000, 1000, QImage.Format_ARGB32)
        painter.drawImage(self.rect, Image1, self.rect)
    def paint(self, painter, option, widget=None):
      #  painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
       # painter.fillRect(self.rect, Qt.transparent)
        image_ARGB_3D1 = numpy.dstack([self.image.astype(numpy.uint8), self.image.astype(numpy.uint8), self.image.astype(numpy.uint8), self.alpha])
        image_ARGB_2D1 = numpy.reshape(image_ARGB_3D1,(-1, 1000*4))
        Image1 = QImage(image_ARGB_2D1.data, 1000, 1000, QImage.Format_ARGB32)
        painter.drawImage(self.rect, Image1, self.rect)

