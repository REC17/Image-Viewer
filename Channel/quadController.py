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
quadController.py

Created by Roger Conturie 2011-07-12
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from quadView import QuadView

class QuadController():
    def __init__(self, mainWin, compViewList, parent = None):
        self.mainWin = mainWin
        self.compViewList = compViewList
        self.zoom = "+"
        self.enableQuadMag = False

        self.xedit2 = self.mainWin.xedit2
        self.yedit2 = self.mainWin.yedit2

        self.compositeview1 = self.compViewList[0]
        self.compositeview2 = self.compViewList[1]
        self.compositeview3 = self.compViewList[2]
        self.compositeview4 = self.compViewList[3]

        self.compositescene1 = self.compositeview1.scene()
        self.compositescene2 = self.compositeview2.scene()
        self.compositescene3 = self.compositeview3.scene()
        self.compositescene4 = self.compositeview4.scene()


        self.compinstanceL = []

    def createConnections(self):
        self.mainWin.keyPressEvent = self.keyPressed
        self.mainWin.keyReleaseEvent = self.keyReleased
        self.mainWin.MagnifyPushButton.pressed.connect(self.magnifyPB)
        self.mainWin.SearchButton2.pressed.connect(self.searchPB)

    def magnifyPB(self):
        if self.enableQuadMag == False:
            self.mainWin.MagnifyPushButton.setText("Turn Off Magnifying Glass")
            self.enableQuadMag = True
            return
        if self.enableQuadMag == True:
            self.mainWin.MagnifyPushButton.setText("Turn On Magnifying Glass")
            self.enableQuadMag = False
            return

    def keyPressed(self, event):
        if event.key() == 16777248:
            self.zoom = "-"

    def keyReleased(self, event):
        if event.key() == 16777248:
            self.zoom = "+"

    def searchPB(self):
        x = self.xedit2.text()
        y = self.yedit2.text()
        itemlist = self.compositeview1.items() + self.compositeview2.items()\
                        + self.compositeview3.items()\
                        + self.compositeview4.items()
        if x == '' or y == '':
            pass
        else:
            for item in itemlist:
                if str(item.__class__.__name__) == "QuadView":
                    try:
                        item.searchExecuted(x, y)
                    except:
                        print "Invalid Type"
                        break

    def displayChannels(self, image_8bit1, image_8bit2, image_8bit3, image_8bit4, zero_array, alpha_array):


        self.QV1 = QuadView(self, image_8bit1, zero_array, alpha_array, \
                            self.compositeview1, self.mainWin.label11, \
                            self.mainWin.SelectedTextBrowser_2, self.mainWin.LivetextBrowser_2)
        self.compositescene1.clear()
        self.compositescene1.addItem(self.QV1)
        
        self.compositeview1.resetMatrix()
        matrix = self.compositeview1.matrix()
        horizontal = 0.5
        vertical = 0.5
        matrix.scale(horizontal, vertical)
        self.compositeview1.setMatrix(matrix)
        
        self.QV2 = QuadView(self, image_8bit2, zero_array, alpha_array,\
                            self.compositeview2, self.mainWin.label12,\
                            self.mainWin.SelectedTextBrowser_2, self.mainWin.LivetextBrowser_2)
        self.compositescene2.clear()
        self.compositescene2.addItem(self.QV2)

        self.compositeview2.setMatrix(matrix)
        

        self.QV3 = QuadView(self, image_8bit3, zero_array, alpha_array,\
                            self.compositeview3, self.mainWin.label21,\
                            self.mainWin.SelectedTextBrowser_2, self.mainWin.LivetextBrowser_2)
        self.compositescene3.clear()
        self.compositescene3.addItem(self.QV3)
        self.compositeview3.setMatrix(matrix)
        

        self.QV4 = QuadView(self, image_8bit4, zero_array, alpha_array,\
                            self.compositeview4, self.mainWin.label22,\
                            self.mainWin.SelectedTextBrowser_2, self.mainWin.LivetextBrowser_2)
        self.compositescene4.clear()
        self.compositescene4.addItem(self.QV4)
        self.compositeview4.setMatrix(matrix)


