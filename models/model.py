
from PySide6.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from PySide6 import QtGui, QtCore
import random
import pygame
from PySide6.QtCore import Qt, QTimer, QTime
from views.view import TaquinGrid, TaquinKey

class Taquin(QWidget):
    def __init__(self):
        super().__init__()
        self.size = 4
        self.layout = QVBoxLayout()
        self.setLayout(self.layout) 
        self.keyboard  = TaquinGrid()
        self.layout.addWidget(self.keyboard)
        self.setGeometry(0,0,600,600)
        self.setMaximumSize(600,600)
        
        self.setWindowTitle("Le jeu de Taquin de LBC") # not leboncoin its Laure Brandy Cecilia
        self.setFont(QFont("Arial", 20))
        self.setStyleSheet("background-color:gray")
        self.label_time = QLabel()
        self.layout_bas = QHBoxLayout() 
        self.setLayout(self.layout_bas)
        self.layout.addLayout(self.layout_bas)
        self.layout_bas.setSpacing(0)
        self.layout_bas.addWidget(self.label_time)  # add label 
        self.reset = QPushButton("RESET")
        self.layout_bas.addWidget(self.reset)
        self.reset.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.reset.clicked.connect(self.redemarre)
        self.label_gagne = QLabel()
        self.layout_bas.addWidget(self.label_gagne)
        self.liste = []
        for i in range(16-1): #afficher les 15 images
            # self.layout_grid.addWidget(TaquinKey(img=f'img/image{i+1}.jpg'))
            # self.layout_grid.addWidget(TaquinKey(img=f'img/image{i+1}.jpg'), i//4,i%4) #i%4 fera 0,1,2,3
            self.liste.append(i+1)
        
        self.liste_cpy = self.liste.copy() # copy of the ordered list to be compared later, finish condition
        self.liste.append(0) #pour avoir lmes 16 valeurs  # to get the 16th value, the free cell
        
        random.shuffle(self.liste_cpy)
        self.liste_cpy.append(0)
        print(self.liste)
        print(self.liste_cpy)
        
        self.keyboard.display_grid(self.liste_cpy)

        pygame.init()#jouer de la musique

    def redemarre(self):
        self.liste_cpy.pop(self.get_zero_index())
        random.shuffle(self.liste_cpy) #on remelange
        self.label_time.setText("") #on remet le label du timer à vide
        self.current_time = 0 #le compteur on le remet a 0
        self.is_good()
        self.keyboard.display_grid(self.liste_cpy)
        self.liste_cpy.append(0)
        self.timer.start()

    def is_good(self):
        if(self.liste_cpy == self.liste): #on compare la liste à celle ordonnée pour verifier si le jeu est fini
            self.label_gagne.setText("!!! YOUPLI DA PLIDOU C'EST GAGNÉ !!!")
            self.label_gagne.setStyleSheet("color : purple; font-size:18px")
            self.timer.stop()
            return True
        else:
            self.label_gagne.setText("")
            return False


    #fonction de déplacments
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        if self.is_good(): return
        lezard = event.key()
        # print(lezard)
        if lezard == QtCore.Qt.Key.Key_Up:
            #print('↑')
            self.arrow_up() 
        elif lezard == QtCore.Qt.Key.Key_Left:
            #print('←')
            self.arrow_left()
        elif lezard == QtCore.Qt.Key.Key_Down:
            #print('↓')
            self.arrow_down()
        elif lezard == QtCore.Qt.Key.Key_Right:
            #print('→')
            self.arrow_right()
        r = self.is_good()
        # print(r)
        return r

    def arrow_right(self):
        zero_index = self.get_zero_index() # on le stocke pcq on s en sert plusieurs fois
        if(zero_index%self.size >= 1):
            self.liste_cpy[zero_index], self.liste_cpy[zero_index-1] = self.liste_cpy[zero_index-1], self.liste_cpy[zero_index]
            self.keyboard.display_grid(self.liste_cpy)

    def arrow_left(self):
        zero_index = self.get_zero_index()
        if(zero_index%self.size < 3):
            self.liste_cpy[zero_index], self.liste_cpy[zero_index + 1] = self.liste_cpy[zero_index + 1], self.liste_cpy[zero_index]
            self.keyboard.display_grid(self.liste_cpy)

    def arrow_down(self):
        zero_index = self.get_zero_index()
        if(zero_index//self.size > 0):
            self.liste_cpy[zero_index], self.liste_cpy[zero_index - self.size] = self.liste_cpy[zero_index - self.size], self.liste_cpy[zero_index]
            self.keyboard.display_grid(self.liste_cpy)

    def arrow_up(self):
        # print("arrow up!")
        zero_index = self.get_zero_index()
        # print("zero index = ", zero_index)
        if((zero_index//self.size) < (self.size-1)):
            self.liste_cpy[zero_index], self.liste_cpy[zero_index + self.size] = self.liste_cpy[zero_index + self.size], self.liste_cpy[zero_index]
            self.keyboard.display_grid(self.liste_cpy)

    def get_zero_index(self):
        return self.liste_cpy.index(0)
    
    
    
    def musique(self):
        # QSound bells("musique/audio_loosers.mp3")
        # self.bells.play()
        self.musique=pygame.mixer.Sound('musique/audio-loosers_coupe.mp3')
        self.musique.play()

    def timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)  # update the timer per second
        self.current_time = 0

    def showTime(self) -> None:
        self.current_time += 1
        self.label_time.setText(f'{self.current_time}s')

