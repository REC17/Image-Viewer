import time
import v4l2capture
import select
from rectItem import RectangleSection
from PIL import Image
from vidImage import VidImage
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class VideoController():
    def __init__(self, mainWin, parent = None):
        self.mainWin = mainWin
        self.videoview = self.mainWin.VideoStreamWindow
        self.videoscene = QGraphicsScene()
        self.videoscene.setSceneRect(QRectF(0, 0, 1280, 800))
        self.videoview.setScene(self.videoscene)
        self.size_x = 0
        self.size_y = 0
        self.video = None
        self.devImg = None
        self.dispGI = None
        self.rs = None
        self.timer = QTimer()

    def createConnections(self):
        QObject.connect(self.timer, SIGNAL("timeout()"), self.updateVideo)
        self.videoview.mousePressEvent = self.videoViewPress
        self.videoview.mouseReleaseEvent = self.videoViewRelease
        self.videoview.mouseMoveEvent = self.videoViewMove        
        self.mainWin.lvStartPB.pressed.connect(self.lvStartPB)
        self.mainWin.lvStopPB.pressed.connect(self.lvStopPB)

    def videoViewPress(self, event):
        if event.button() == 1:
            x, y = event.pos().x(), event.pos().y()
            mapScene =  self.videoview.mapToScene(x, y)
            x, y = mapScene.x(), mapScene.y()

            position = QPointF(x, y)
            self.rs = RectangleSection(position)
            self.rs.setPos(position)
            self.videoscene.addItem(self.rs)

        if event.button() == 2:

            matrix = self.videoview.matrix()
            matrix.reset()
            self.videoview.setMatrix(matrix)

    def videoViewRelease(self, event):

        if event.button() == 1:
            #self.videoscene.removeItem(self.rs)
            x = self.rs.position.x()
            y = self.rs.position.y()
            width = self.rs.width
            height = self.rs.height
            matrix = self.videoview.matrix()
            matrix.reset()
            matrix.scale(1280/width, 800/height)
            self.videoview.setMatrix(matrix)
            self.videoview.centerOn(x + 0.5*width, y + 0.5*height)
            self.videoscene.removeItem(self.rs)            
            self.rs = None

    def videoViewMove(self, event):

        if self.rs != None:
            x, y = event.pos().x(), event.pos().y()
            mapScene =  self.videoview.mapToScene(x, y)
            x, y, = mapScene.x(), mapScene.y()
            aspRNum = x - self.rs.x()
            aspRDom = y - self.rs.y()
            if aspRNum > 0 and aspRDom > 0:    
                aspectRatio = self.dispGI.boundingRect().width()/self.dispGI.boundingRect().height()
                appliedRatio = aspRNum/aspRDom
                if appliedRatio >= aspectRatio:
                    self.rs.height = y - self.rs.y()
                    self.rs.width = 1.6*(y - self.rs.y())
                if appliedRatio < aspectRatio:
                    self.rs.width = x - self.rs.x()
                    self.rs.height = (x - self.rs.x())/aspectRatio
                self.rs.update()
            else:
                self.rs.width = 1
                self.rs.height = 1
                self.rs.update()
            
    def updateVideo(self):
        try:
            select.select((self.video,), (), ())
            image_data = self.video.read_and_queue()
            self.videoscene.removeItem(self.dispGI)
            self.devImg = QImage(image_data, self.size_x, self.size_y,\
                                                         QImage.Format_RGB888)
            self.devImg.bits() #Necessary to prevent Seg Fault (unknown why)
            target = QRectF(0, 0, self.devImg.width(), self.devImg.height())
            source = QRectF(0, 0, self.devImg.width(), self.devImg.height())
            self.dispGI = VidImage(self, target, self.devImg, source)
            self.videoscene.addItem(self.dispGI)
            self.dispGI.setZValue(-1)
            self.videoscene.update()
        except:
            pass

    def lvStartPB(self):

        self.video = v4l2capture.Video_device("/dev/video0")
        self.size_x, self.size_y = self.video.set_format(1280, 800)
        self.video.create_buffers(1)
        self.video.queue_all_buffers()
        self.video.start()
        select.select((self.video,), (), ())
        image_data = self.video.read_and_queue()
        self.devImg = QImage(image_data, self.size_x, self.size_y,\
                                                     QImage.Format_RGB888)
        self.devImg.bits() #Necessary to prevent Seg Fault (unknown why)
        target = QRectF(0, 0, self.devImg.width(), self.devImg.height())
        source = QRectF(0, 0, self.devImg.width(), self.devImg.height())
        self.dispGI = VidImage(self, target, self.devImg, source)
        self.videoscene.clear()
        self.videoscene.addItem(self.dispGI)
        self.dispGI.setZValue(-1)
        self.videoscene.update()
        self.timer.start()

    def lvStopPB(self):

        self.timer.stop()
