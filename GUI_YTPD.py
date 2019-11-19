from __future__ import unicode_literals
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
    QTextEdit, QGridLayout, QApplication, QPushButton, QFileDialog, QProgressBar)
import pytube, youtube_dl, os, sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        #Qt objects in GUI
        self.lbPlayList = QLabel('Play List Link:')
        self.lbPlayList.setFont(self.getFont())
        self.lbSelFolder = QLabel('Doanload Folder:')
        self.lbSelFolder.setFont(self.getFont())
        self.lbStatus = QLabel()
        self.lbStatus.setFont(self.getFont())
        
        self.lnEditPlayList = QLineEdit()
        self.lnEditSelFolder = QLineEdit()
        self.btnSelFolder = QPushButton('Select Folder')
        self.btnControl = QPushButton('Start')

        self.processBar = QProgressBar(self)
        self.processBar.setValue(0)

        #signals and solt connected
        self.btnSelFolder.clicked.connect(self.selectFolder)
        self.btnControl.clicked.connect(self.run)

        #put the object in the grid
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.lbPlayList, 1, 0, QtCore.Qt.AlignRight)
        grid.addWidget(self.lnEditPlayList, 1, 1, 1, 2)

        grid.addWidget(self.lbSelFolder, 2, 0)
        grid.addWidget(self.lnEditSelFolder, 2, 1)
        grid.addWidget(self.btnSelFolder, 2, 2)
        
        grid.addWidget(self.processBar, 3, 1)
        grid.addWidget(self.btnControl, 3, 2)

        #set the layout and the window
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 650, 100)
        self.setWindowTitle('YTPD')    
        self.show()

    def getFont(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        return font
    
    def getLink(self):
        return self.lnEditPlayList.text()

    def getPath(self):
        return self.lnEditSelFolder.text()

    def selectFolder(self):
        filePath = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lnEditSelFolder.setText(filePath)
    
    def run(self):
        self.threadclass = ThreadClass()
        self.threadclass.setPath(self.getPath())
        self.threadclass.setLinkList(self.getLink())
        self.threadclass.change_value.connect(self.processBar.setValue)
        self.threadclass.start()


class ThreadClass(QtCore.QThread):
    def __init__(self, parent = None):
        return super().__init__(parent)

    change_value = QtCore.pyqtSignal(int)

    def setPath(self, path):
        os.chdir(path)

    def setLinkList(self, link):
        self.linkList = link
        self.links = self.makePlayList(link)

    def makePlayList(self, link):
        pl = pytube.Playlist(link)
        pl.populate_video_urls()
        links = pl.video_urls
        return links

    def run(self):
        a = 1
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        self.change_value.emit(int((a*100)/len(self.links)))
        for link in self.links:
            a = a + 1
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                self.change_value.emit(int((a*100)/len(self.links)))
                



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()