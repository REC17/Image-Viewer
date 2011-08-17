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
rectItem.py

Created by Roger Conturie 2011-07-12
"""

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
