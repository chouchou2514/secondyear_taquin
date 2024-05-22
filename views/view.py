import PySide6
from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QGridLayout, QSizePolicy, QToolButton
from PySide6.QtGui import QPixmap
from PySide6 import QtCore
from models.image import ImBtn


class TaquinKey(QPushButton): #class for create the buttons
    def __init__(self, text: str = '', img: str = ''): #instantiation
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        pixmap = QPixmap(img)
        self.label = QLabel()
        self.lay = QVBoxLayout()
        self.label.setPixmap(pixmap)
        self.lay.addWidget(self.label)
        self.lay.setContentsMargins(0,0,0,0)
        self.setLayout(self.lay)
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)


class TaquinGrid(QWidget): #class for the grid of the game, place the buttons
    def __init__(self):
        super().__init__()
        # self.layout_grid = QGridLayout()
        # self.setLayout(self.layout_grid)
        # self.layout_grid.addWidget(TaquinKey("1"), 0, 0, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("2"), 0, 1, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("3"), 0, 2, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("4"), 0, 3, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("5"), 1, 0, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("6"), 1, 1, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("7"), 1, 2, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("8"), 1, 3, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("9"), 2, 0, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("10"), 2, 1, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("11"), 2, 2, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("12"), 2, 3, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("13"), 3, 0, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("14"), 3, 1, 1, 1)
        # self.layout_grid.addWidget(TaquinKey("15"), 3, 2, 1, 1)
        ImBtn.couper_image("img/antoine.jpg")
        self.layout_grid = QGridLayout()
        self.setLayout(self.layout_grid) 


    def display_grid(self, list):
        for i in reversed(range(self.layout_grid.count())): 
            self.layout_grid.itemAt(i).widget().setParent(None) # clear tout les widget, on reppart d'une nouvelle grille # clear all the widgets within the layout

        compteur = 0
        for elt in list:
            if elt != 0:# for all cases with an image
                self.layout_grid.addWidget(TaquinKey(img=f'img/image{elt}.jpg'), compteur//4,compteur%4) # place the image widget
            compteur +=1
        

