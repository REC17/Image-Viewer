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
distanceLine.py

Created by Roger Conturie 2011-07-12
"""


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
