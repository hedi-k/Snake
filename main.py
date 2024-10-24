#coding:utf-8

#Title: Snake
#Authors: Hedi
#Date: 22/10/2024

import tkinter #Pour l'usage de la fenêtre
import random

#Constantes
ROWS = 25
COLS = 25
TILE_SIZE =25
#Taille de la fenêtre
WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

#Classe pour la construction des objets (serpent et nourritures)
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Fenêtre du jeu
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False) #Empêche la modification de la taille de la fenêtre
canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0) #Zone de dessin 
canvas.pack() #Ajout le canvas a la fenêtre principal (window)
window.update() #méthode qui force tkinter à mettre à jour l'interface graphique

#Centrer l'application
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
#geometry permet d'affecter les coordonnées de l'application calculés précedement mais utilise un formatage particulier w h x y
window.geometry("{}x{}+{}+{}".format(window_width, window_height, window_x, window_y))

#Initialise le jeu
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
snake_body =[]
food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)
velocityX = 0
velocityY = 0
game_over = False
score = 0

#gestion de la direction, va incrémenter ou décrémenter x et y en fonction de la touche utilisé.
#e = event
def change_direction(e):
    global velocityX, velocityY, game_over
    
    if (game_over):
        return
    #print(e) pour faire des tests sur les touches et les informations remontées
    #print(e.keysym) #limite le nombre d'informations au minimum
    #les conditions permettent de s'assurer un déplacement cohérent avec un snake, l'empêcher de faire marche arrière
    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0
        
#Déplace le serpent en modifiant x et y en fonction de la touche préssé qui dépend de change_direction()
def move():
    #global -> référence à snake plus haut 
    global snake,food, snake_body, game_over, score
    if (game_over):
        return

    if (snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height):
        game_over = True
        return
        
    for tile in snake_body:
        if(snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return
            
    #Controle collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 1
    #Gestion du corps
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if(i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y
            
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE


#Dessine le serpent et la nourriture
def draw():
    global snake, score #global -> référence à snake plus haut
    
    move()
    #Pour "rafchaichir" la fenêtre en supprimant les anciens dessins
    canvas.delete("all")
    #L'ordre est important pour l'affichage (Ainsi les derniers seront les premiers, et les premiers les derniers)
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "red")
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green")
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "lime green")
        
    if (game_over):
        canvas.create_text(window_width/2, window_width/2, font ="Arial 20", text ="Game Over : {}".format(score), fill = "white")
    window.after(100, draw) #Appel la fonction tout les 100ms

draw()

#key listner
window.bind("<KeyRelease>", change_direction)
window.mainloop() #Permet à l'application de rester ouverte, d'écouter et de répondre aux événements, et de maintenir l'interface graphique active.