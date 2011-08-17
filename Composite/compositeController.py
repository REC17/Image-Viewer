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
compositeController.py

Created by Roger Conturie 2011-07-12
"""

import os
import sys
import math
import numpy
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from compositeImage import CompImage
from Channel.quadController import QuadController

class CompositeController():
    def __init__(self, mainWin, compViewList, parent = None): 
        self.mainWin = mainWin
        self.compViewList = compViewList
        self.cParser = self.mainWin.cParser
        self.currentDir = self.mainWin.currentDir
        
        self.quadC = QuadController(self.mainWin, self.compViewList)
        self.quadC.createConnections()

        self.dotpermission = False
        self.lastcircle = []
        self.lastline = None

        self.C1Def = self.mainWin.C1Def
        self.C2Def = self.mainWin.C2Def
        self.C3Def = self.mainWin.C3Def
        self.C4Def = self.mainWin.C4Def             
        self.comboBox = self.mainWin.comboBox


        self.view = self.mainWin.graphicsView
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        
        self.selectedbrowser = self.mainWin.SelectedTextBrowser
        self.livebrowser = self.mainWin.LivetextBrowser
        self.pixelValueBrowser = self.mainWin.pixelValueBrowser

        self.compositeview1 = self.compViewList[0]
        self.compositeview2 = self.compViewList[1]
        self.compositeview3 = self.compViewList[2]
        self.compositeview4 = self.compViewList[3]

        

    def createConnections(self):
        self.mainWin.DotOn.pressed.connect(self.dotOn)
        self.mainWin.ClearButton.pressed.connect(self.clearButtonPressed)
        self.mainWin.LoadComposite.pressed.connect(self.loadCompositeButtonPressed)
        self.mainWin.DotOff.pressed.connect(self.dotOff)
        self.mainWin.ClearDots.pressed.connect(self.clearDots)

    def clearButtonPressed(self):

        self.lastcircle = []
        self.lastline = None
        self.scene.clear()
        if self.comboBox.currentText() == "All":
            self.loadinit("A", "Clear")
        if self.comboBox.currentText() == "3 Channels":
            self.loadinit("3C", "Clear")
        if self.comboBox.currentText() == "Channel 1":
            self.loadinit("1", "Clear")
        if self.comboBox.currentText() == "Channel 2":
            self.loadinit("2", "Clear")
        if self.comboBox.currentText() == "Channel 3":
            self.loadinit("3", "Clear")
        if self.comboBox.currentText() == "Channel 4":
            self.loadinit("4", "Clear")
  
            
    def loadCompositeButtonPressed(self):
        self.lastcircle = []
        self.lastline = None

        if self.comboBox.currentText() == "All":
            self.loadinit("A", "Load")
        if self.comboBox.currentText() == "3 Channels":
            self.loadinit("3C", "Load")
        if self.comboBox.currentText() == "Channel 1":
            self.loadinit("1", "Load")
        if self.comboBox.currentText() == "Channel 2":
            self.loadinit("2", "Load")
        if self.comboBox.currentText() == "Channel 3":
            self.loadinit("3", "Load")
        if self.comboBox.currentText() == "Channel 4":
            self.loadinit("4", "Load")
        
    def loadinit(self, type, mode):
        self.cParser.read(self.currentDir+"/.config/.polImgPro.cfg")
        if mode == "Load":
            if type == "1" or type == "A" or type == "3C":
                if self.C1Def.isChecked() == True:
                    self.path1 = self.cParser.get('PREFIMGPATHS','Path1')
                else:
                    self.path1 = QFileDialog.getOpenFileName(self, \
                            "Open File", self.path , str("Images (*raw)"))
                self.mainWin.c1label.setText(str(self.path1.split("/")[-1]))

            if type == "2" or type == "A" or type == "3C":
                if self.C2Def.isChecked() == True:
                    self.path2 = self.cParser.get('PREFIMGPATHS','Path2')
                else:     
                    self.path2 = QFileDialog.getOpenFileName(self, \
                            "Open File", self.path , str("Images (*raw)"))
                self.mainWin.c2label.setText(str(self.path2.split("/")[-1]))

            if type == "3" or type == "A" or type == "3C":
                if self.C3Def.isChecked() == True:
                    self.path3 = self.cParser.get('PREFIMGPATHS','Path3')
                else:
                    self.path3 = QFileDialog.getOpenFileName(self, \
                            "Open File", self.path , str("Images (*raw)"))
                self.mainWin.c3label.setText(str(self.path3.split("/")[-1]))

            if type == "4" or type == "A":
                if self.C4Def.isChecked() == True:
                    self.path4 = self.cParser.get('PREFIMGPATHS','Path4')
                else:
                    self.path4 = QFileDialog.getOpenFileName(self, \
                            "Open File", self.path , str("Images (*raw)"))
                self.mainWin.c4label.setText(str(self.path4.split("/")[-1]))

        if mode == "Clear":
            if type == '1' or type == 'A' or type == '3C':
                self.path1 = None
                self.c1label.setText('')
            if type == '2' or type == 'A' or type == '3C':
                self.path2 = None
                self.c2label.setText('')
            if type == '3' or type == 'A' or type == '3C':
                self.path3 = None
                self.c3label.setText('')
            if type == '4' or type == 'A':
                self.path4 = None
                self.c4label.setText('')

        self.imageGenerator(self.path1, self.path2, self.path3, self.path4)

    def imageGenerator(self, path1, path2, path3, path4):
        width = 1000
        height = 1000
        shape = (width, height)
        alpha_array = 255*(numpy.ones(shape, dtype=numpy.uint8))
        zero_array = numpy.zeros(shape, dtype=numpy.uint8)
        
        Red = zero_array
        Blue = zero_array
        Green = zero_array
        Yellow = zero_array
        Cyan = zero_array
        Magenta = zero_array
        White = zero_array
 
        image_array_2D1 = zero_array
        
        #Blue
        try:
            image_file = open(path1)
            # load a 1000000 length array
            image_array_1D1 = numpy.fromfile(file=image_file,\
                                                dtype=numpy.uint16)
            image_file.close()
            image_array_2D1 = image_array_1D1.reshape(shape)
            image_8bit1 = (image_array_2D1 >> 6)

        except:
            print "Except 1"
            image_8bit1 = 0*alpha_array
        
        #Green
        try:
            image_file = open(path2)
            # load a 1000000 length array
            image_array_1D2 = numpy.fromfile(file=image_file,\
                                                dtype=numpy.uint16)
            image_file.close()
            image_array_2D2 = image_array_1D2.reshape(shape)
            image_8bit2 = (image_array_2D2 >> 6)
        except:
            print "Except 2"
            image_8bit2 = 0*alpha_array         
        
        try:
            image_file = open(path3)
            image_array_1D3 = numpy.fromfile(file=image_file,\
                                                dtype=numpy.uint16)
            image_file.close()
            image_array_2D3 = image_array_1D3.reshape(shape)
            image_8bit3 = (image_array_2D3 >> 6)
        except:
            print "Except 3"
            image_8bit3 = 0*alpha_array
            image_array_2D3 = alpha_array.reshape(shape)
        
            
        #George

        try:
            image_file = open(path4)
            # load a 1000000 length array
            image_array_1D4 = numpy.fromfile(file=image_file,\
                                                dtype=numpy.uint16)
            image_file.close()
            image_array_2D4 = image_array_1D4.reshape(shape)
            image_8bit4 = (image_array_2D4 >> 6)
        except:
            print "Except 4"
            image_8bit4 = 0*alpha_array


        channelcombolist = [self.mainWin.channel1combobox, self.mainWin.channel2combobox,\
                                self.mainWin.channel3combobox, self.mainWin.channel4combobox]
        imagelist = [image_8bit1, image_8bit2, image_8bit3, image_8bit4]
        for item in range(4):
            if channelcombolist[item].currentText() == "Red":
                Red = Red + imagelist[item]
            elif channelcombolist[item].currentText() == "Blue":
                Blue = Blue + imagelist[item]
            elif channelcombolist[item].currentText() == "Green":
                Green = Green + imagelist[item]
            elif channelcombolist[item].currentText() == "Yellow":
                Yellow = Yellow + imagelist[item]
            elif channelcombolist[item].currentText() == "Cyan":
                Cyan = Cyan + imagelist[item]
            elif channelcombolist[item].currentText() == "Magenta":
                Magenta = Magenta + imagelist[item]
            elif channelcombolist[item].currentText() == "White":
                White = White + imagelist[item]
       
        
        image_ARGB_3D = numpy.dstack([(Blue + Cyan + Magenta + White)\
                                        .clip(0,255).astype(numpy.uint8),\
                                        (Green + Cyan + Yellow + White)\
                                        .clip(0,255).astype(numpy.uint8),\
                                        (Red + Magenta + Yellow + White)\
                                        .clip(0,255).astype(numpy.uint8),\
                                        alpha_array])
        
        # reshape to a 2D array that has 4 bytes per pixel
        image_ARGB_2D = numpy.reshape(image_ARGB_3D,(-1,width*4))
 
        #Numpy buffer QImage declaration
        Image = QImage(image_ARGB_2D.data, width, height, QImage.Format_ARGB32)
        Image.ndarray = image_ARGB_2D  

        target = QRectF(0, 0, Image.width(), Image.height())
        source = QRectF(0, 0, Image.width(), Image.height())
    
        compImage = CompImage(self.mainWin, self, target, Image, source,\
                                self.selectedbrowser, self.livebrowser, \
                                self.pixelValueBrowser, image_array_2D1) 
        self.scene.clear()
        self.scene.addItem(compImage)
        self.Image = Image

        self.quadC.displayChannels(image_8bit1, image_8bit2, image_8bit3, image_8bit4, zero_array, alpha_array)


    def dotOn(self):
        self.dotpermission = True
        self.mainWin.DotOff.setEnabled(True)
        self.mainWin.DotOn.setEnabled(False)

    def dotOff(self):
        self.dotpermission = False
        self.mainWin.DotOff.setEnabled(False)
        self.mainWin.DotOn.setEnabled(True)

    def clearDots(self):
        imageitems = self.scene.items()
        for item in imageitems:
            if str(item.__class__.__name__) == "DistanceLine"\
                or str(item.__class__.__name__) == "CircleMarker":
                self.scene.removeItem(item)
        self.scene.update()

        self.lastline = None

        self.lastcircle = []
    
