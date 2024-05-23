
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
        self.size = 4       #size 4*4
        self.layout = QVBoxLayout()  #main layout of the tease
        self.setLayout(self.layout)  #add the layout
        self.keyboard  = TaquinGrid() #the game will be a grid
        self.layout.addWidget(self.keyboard) #we add the keyboard
        self.setGeometry(0,0,600,600) #size of the main window
        self.setMaximumSize(600,600)  #maximum size of the window
        
        self.setWindowTitle("Le jeu de Taquin de LBC") # not leboncoin its Laure Brandy Cecilia
        self.setFont(QFont("Arial", 20)) #font
        self.setStyleSheet("background-color:gray") #background of the game
        self.label_time = QLabel() #timer is a label
        self.layout_bas = QHBoxLayout() #secondary layout
        self.setLayout(self.layout_bas) #set the layout
        self.layout.addLayout(self.layout_bas) #add the layout to the mail layout
        self.layout_bas.setSpacing(0) #space the layout_bas game low
        self.layout_bas.addWidget(self.label_time)  # add label  time
        self.reset = QPushButton("RESET") # create the reset button
        self.layout_bas.addWidget(self.reset) #we add the reset button to the layout_bas
        self.reset.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus) #no focus on the reset button
        self.reset.clicked.connect(self.redemarre) #link the reset button to the "redemarre" function
        self.label_gagne = QLabel() #the sentance for win is a label
        self.layout_bas.addWidget(self.label_gagne) #we add the label to the layout_bas
        self.liste = [] #create the empty list
        for i in range(16-1): #fill the list
            # self.layout_grid.addWidget(TaquinKey(img=f'img/image{i+1}.jpg'))
            # self.layout_grid.addWidget(TaquinKey(img=f'img/image{i+1}.jpg'), i//4,i%4) #i%4 fera 0,1,2,3
            self.liste.append(i+1)
        
        self.liste_cpy = self.liste.copy() # copy of the ordered list to be compared later, finish condition
        self.liste.append(0) #pour avoir lmes 16 valeurs  # to get the 16th value, the free cell
        
        #random.shuffle(self.liste_cpy) # randomizing the list, =images
        self.liste_cpy.append(0) # empty cell at the bottom right corner
        # print(self.liste)
        # print(self.liste_cpy)
        
        self.keyboard.display_grid(self.liste_cpy) # display the grid

        pygame.init()#jouer de la musique # play the music

    def redemarre(self):
        '''
        restarts the game when pressing reset button
        '''
        self.liste_cpy.pop(self.get_zero_index()) # removing zero
        random.shuffle(self.liste_cpy) #on remelange # shuffle
        self.label_time.setText("") #on remet le label du timer à vide # reset the timer
        self.current_time = 0 #le compteur on le remet a 0 # setting it at zero
        self.is_good() #check if we win or not
        self.keyboard.display_grid(self.liste_cpy) #we display the grid for the new game
        self.liste_cpy.append(0) # placing the empty cell
        self.timer.start() #start the timer

    def is_good(self):
        """
        check if we win or not
        :return: Bool
        """
        if(self.liste_cpy == self.liste): #on compare la liste à celle ordonnée pour verifier si le jeu est fini # compaaring the actual list to the finished state list
            self.label_gagne.setText("!!! YOUPLI DA PLIDOU C'EST GAGNÉ !!!")
            self.label_gagne.setStyleSheet("color : purple; font-size:18px")
            self.timer.stop()
            return True
        else:
            self.label_gagne.setText("")
            return False


    #connected the game to the keyboard arrows
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        keyboard controls
        :param event:
        :return:
        """
        self.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus) #forcing the focus of the window
        if self.is_good(): return #can't move if the game is finish
        lezard = event.key() #lezard take the value of the key we press on the keyboard
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
        zero_index = self.get_zero_index() #get the index of the empty box
        if(zero_index%self.size >= 1): #condition for moving
            self.liste_cpy[zero_index], self.liste_cpy[zero_index-1] = self.liste_cpy[zero_index-1], self.liste_cpy[zero_index] #we swap the 2 images
            self.keyboard.display_grid(self.liste_cpy) #display the grid after the movment

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
        """
        get the index of the empty cell
        :return: the value of the index of the empty cell
        """
        return self.liste_cpy.index(0)
    
    
    
    def musique(self):
        '''
        put music while we playing
        :return:
        '''
        # QSound bells("musique/audio_loosers.mp3")
        # self.bells.play()
        self.musique=pygame.mixer.Sound('musique/audio-loosers_coupe.mp3')
        self.musique.play()

    def timer(self):
        '''
        create a timer while we playing
        :return:
        '''
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)  # update the timer per second
        self.current_time = 0

    def showTime(self) -> None:
        '''
        display the timer
        :return:
        '''
        self.current_time += 1
        self.label_time.setText(f'{self.current_time}s')

