# 🧩 Projet Taquin - ISEN Caen (LBC Edition)

Ce dépôt contient le projet de **Jeu du Taquin** réalisé en deuxième année. L'objectif était de créer un puzzle coulissant interactif avec une interface graphique Qt, en respectant une architecture propre et modulaire.

## 👥 Le trinôme
Projet réalisé par : **Laure, Brandy et Cécilia**.

## 🛠️ Architecture du Projet (Modèle MVC)
Le projet est divisé en plusieurs blocs logiques pour une meilleure maintenabilité :

1. **Le Contrôleur (`controller.py`)** : Le chef d'orchestre. Il initialise l'application, lance la musique, le timer et affiche la fenêtre principale.
2. **Le Modèle (`models/model.py`)** : Contient toute la logique métier.
   - Gestion de la grille (4x4).
   - Algorithmes de déplacement des cases (haut, bas, gauche, droite).
   - Gestion du multimédia (sons via `pygame`) et du chronomètre (`QTimer`).
3. **La Gestion d'Image (`image.py`)** : Un module dédié qui utilise la bibliothèque **Pillow (PIL)** pour :
   - Charger une image source.
   - La recadrer en carré et la redimensionner en 600x600.
   - La découper chirurgicalement en 16 vignettes (`image1.jpg` à `image16.jpg`) stockées dans le dossier `img/`.
4. **La Vue (`views/view.py`)** : Gère l'affichage des boutons et de la grille interactive.



[Image of Model-View-Controller architecture diagram]


## 🚀 Fonctionnalités
- **Interface Qt (PySide6)** : Une fenêtre grise élégante de 600x600 pixels.
- **Découpage Dynamique** : Capacité de transformer n'importe quelle photo en puzzle.
- **Système de Timer** : Affiche le temps écoulé pour défier vos amis.
- **Ambiance Sonore** : Musique intégrée (`audio-loosers_coupe.mp3`) pour accompagner la partie.
- **Clavier & Souris** : Logique de déplacement fluide des cases.

## 🔧 Installation et Lancement

1. **Prérequis** : Assurez-vous d'avoir Python 3.x installé.
2. **Installation des bibliothèques** :
   ```bash
   pip install PySide6 pygame Pillow
