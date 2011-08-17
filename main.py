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
main.py

Created by Roger Conturie 2011-07-12
"""

import os
import sys
from ui import ui_ImageViewerWindow #,png, itertools
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Video.videoController import VideoController
from Composite.compositeController import CompositeController
import ConfigParser

class STBimageviewer(QMainWindow, ui_ImageViewerWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(STBimageviewer, self).__init__(parent)
        self.setupUi(self)
        self.currentDir = os.getcwd()
        self.cParser = ConfigParser.ConfigParser()
        try:
            os.mkdir(self.currentDir+"/.config")
            file(self.currentDir+"/.config/.polImgPro.cfg", 'w')
            self.cParser.add_section('PREFIMGPATHS')
            self.cParser.set('PREFIMGPATHS','Path1','None')
            self.cParser.set('PREFIMGPATHS','Path2','None')
            self.cParser.set('PREFIMGPATHS','Path3','None')
            self.cParser.set('PREFIMGPATHS','Path4','None')
            with open(self.currentDir+"/.config/.polImgPro.cfg", 'w') as \
                configFile:
                self.cParser.write(configFile)
        except:
            pass
        

        self.compositeview1 = self.graphicsView_2
        self.compositescene1 = QGraphicsScene()
        self.compositeview1.setScene(self.compositescene1)

        self.compositeview2 = self.graphicsView_3
        self.compositescene2 = QGraphicsScene()
        self.compositeview2.setScene(self.compositescene2)

        self.compositeview3 = self.graphicsView_4
        self.compositescene3 = QGraphicsScene()
        self.compositeview3.setScene(self.compositescene3)

        self.compositeview4 = self.graphicsView_5
        self.compositescene4 = QGraphicsScene()
        self.compositeview4.setScene(self.compositescene4)


        compViewList = [self.compositeview1,\
                self.compositeview2,\
                self.compositeview3,\
                self.compositeview4]

        self.compC = CompositeController(self, compViewList)
        self.compC.createConnections()



        self.vidC = VideoController(self)
        self.vidC.createConnections()


def main():
    app = QApplication(sys.argv)
    window = STBimageviewer()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
