#coding:utf-8

#Title: Snake
#Authors: Hedi
#Date: 22/10/2024

import tkinter #Pour l'usage de la fenêtre
import random

#Constantes
ROWS = 25
COLS = 25
TITLE_SIZE =25
#Taille de la fenêtre
WINDOW_WIDTH = TITLE_SIZE * COLS
WINDOW_HEIGHT = TITLE_SIZE * ROWS

#Fenêtre du jeu
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False) #Empêche la modification de la taille de la fenêtre

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0) #Zone de dessin 
canvas.pack() #Ajout le canvas a la fenêtre principal (window)
window.update() #méthode qui force tkinter à mettre à jour l'interface graphique

#Centre l'application
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
#geometry permet d'affecter les coordonnées de l'application calculés précedement mais utilise un formatage particulier w h x y
window.geometry("{}x{}+{}+{}".format(window_width, window_height, window_x, window_y))

window.mainloop() #Permet à l'application de rester ouverte, d'écouter et de répondre aux événements, et de maintenir l'interface graphique active.