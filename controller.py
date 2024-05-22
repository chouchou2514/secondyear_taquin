import PySide6
from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout, QGridLayout, QSizePolicy
from PySide6.QtGui import QFont
import time
from models.model import Taquin
from views.view import TaquinGrid
# from models.image import img

if __name__ == "__main__" :
    app = QApplication([])
    taquin = Taquin()
    taquin.musique() 
    taquin.timer()
    taquin.show()
    app.exec()
    # print(taquin.liste)
    # print(taquin.liste_cpy)
   




