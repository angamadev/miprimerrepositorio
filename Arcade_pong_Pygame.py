# Este archivo lo mandop a Bienvenido para comprobar que hago biem un commit en una rama nueva



# Juego de Pong con Pygame

# importar modulos y los iniciamos
import pygame, sys
pygame.init()

class Player:
    def __init__(self,cord_x,cord_y,ancho,alto):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.ancho = ancho
        self.alto = alto
        #self.speed_x = speed_x
        #self.speed_y = speed_y
        #self.speed_y = 1

    def movimiento(self,speed_x,speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        

class Pelota:
    def __init__(self,cord_x_pelota,cord_y_pelota,speed_x_pelota,speed_y_pelota):
        self.cord_x_pelota = cord_x_pelota
        self.cord_y_pelota = cord_y_pelota
        self.speed_x_pelota = speed_x_pelota
        self.speed_y_pelota = speed_y_pelota


# Definimos Colores
BLACK , WHITE, GREEN, RED, BLUE= (0,0,0),(255,255,255),(0,255,0),(255,0,0),(0,0,255)
'''WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)'''

### Crear Ventana
groundcolor = BLUE

# Damos tañaño a la ventana
SCREEN_ANCHO = 1000
SCREEN_ALTO = 800
size = (SCREEN_ANCHO,SCREEN_ALTO)
screen = pygame.display.set_mode(size)
center_x = (SCREEN_ANCHO // 2)
center_y = (SCREEN_ALTO // 2)

# Definir reloj
clock = pygame.time.Clock()

# Cefinimos paleta de los jugadores
paleta1 = Player(30,350,30,130)
paleta2 = Player(940,350,30,130)

# definimos velocidad de las paletas
speed_paleta1 = paleta1.movimiento(0,0)
speed_paleta2 = paleta2.movimiento(0,0)

# Creamos pelota
pelota1 = Pelota(500,400,3,3)

# Inicializamos los Marcadores
score_player1 = 0
score_player2 = 0

# Variables
game_over = False

# Creamos bucle principal de los eventos
while game_over is not True:
    
    for event in pygame.event.get():
        
        # Evento de tocar clicar con el mouse para salir del juego
        if event.type == pygame.QUIT:
            sys.exit()

        
        # ----- Zona Logica ---------

        # Evento para apretar teclas del teclado para controlar las paletas
        if event.type == pygame.KEYDOWN:

            # Player1
            if event.key == pygame.K_w:
                paleta1.speed_y = -3
            if event.key == pygame.K_s:
                paleta1.speed_y = 3 

            # Player2
            if event.key == pygame.K_UP:
                paleta2.speed_y = -3
            if event.key == pygame.K_DOWN:
                paleta2.speed_y = 3 

            # Colision paletas en suelo
            if paleta1.cord_y > 680 or paleta2.cord_y > 680:
                if paleta1.cord_y >= 680:
                    paleta1.cord_y = 680
                if paleta2.cord_y >= 680:
                    paleta2.cord_y = 680

            # Colision de paletas en techo
            if paleta1.cord_y < 0 or paleta2.cord_y < 0:
                if paleta1.cord_y < 0:
                    paleta1.cord_y = 0
                if paleta2.cord_y < 0:
                    paleta2.cord_y = 0
            
        # Evento para soltar las teclas del teclado que controlan las paletas
        if event.type == pygame.KEYUP:

            # Player1
            if event.key == pygame.K_w:
                paleta1.speed_y = 0
            if event.key == pygame.K_s:
                paleta1.speed_y = 0   

             # Player2
            if event.key == pygame.K_UP:
                paleta2.speed_y = 0
            if event.key == pygame.K_DOWN:
                paleta2.speed_y = 0       
       
        pygame.key. set_repeat (10) 

        # Sumar o restar el movimiento para cambiar de posicion las paletas
        paleta1.cord_y += paleta1.speed_y
        paleta2.cord_y += paleta2.speed_y
    
    # Movimiento Pelota
    pelota1.cord_x_pelota += pelota1.speed_x_pelota 
    pelota1.cord_y_pelota += pelota1.speed_y_pelota

    # Colisiones de pelota contra techo y suelo
    if pelota1.cord_y_pelota > 784 or pelota1.cord_y_pelota < 16:
        pelota1.speed_y_pelota = pelota1.speed_y_pelota * (-1)

     # Si pelota toca con las paredes izq o derecha
    if pelota1.cord_x_pelota > 984 or pelota1.cord_x_pelota < 16:

        # Si toca la pared Derecha sumar 1 punto a el marcador del jugador 1
        if pelota1.cord_x_pelota > 984:
            score_player1 += 1
        # Si toca la pared Izquierda sumar 1 punto a el marcador del jugador 2
        if pelota1.cord_x_pelota < 16:
            score_player2 += 1

        # Mostrar el ganador si suma un total de 5 puntos
        if score_player1 == 5 or score_player2 == 5:
            game_over = True

            # Si jugador 1 suma 5 puntos gana la partida
            if score_player1 == 5:
                winner = "Winner PLAYER 1"

            # Si jugador 2 suma 5 puntos gana la partida
            if score_player2 == 5:
                winner = "Winner PLAYER 2"

        # Cambio de direccion (rebota) la pelota si choca contra la paleta de cualquier jugador
        pelota1.speed_x_pelota = pelota1.speed_x_pelota * (-1)

        # Posiciono la pelota en el centro de pantalla
        pelota1.cord_x_pelota = 500
        pelota1.cord_y_pelota = 400

        # Pausa de algun segundo para continuar
        pygame.event.wait(1000)

    # ---- FIN Zona LOGICA -----------

    # Pintar la pantalla en blanco
    screen.fill(BLACK)

    # Pintar Marcador y Resultados
    font = pygame.font.SysFont("serif",45)
    title_score = font.render("Player 1 | Player 2", True, GREEN)
    result_score = font.render(f"{score_player1} | {score_player2}", True, WHITE)
    screen.blit(title_score,[center_x - (title_score.get_width() // 2),100])
    screen.blit(result_score,[center_x - (result_score.get_width()//2),160])

    if game_over:
        font1 = pygame.font.SysFont("serif",60)
        mostrar_winnner = font1.render(f"{winner}", True, RED)
        screen.blit(mostrar_winnner,[center_x - (mostrar_winnner.get_width()//2),center_y])
        
    ### ----------- Zona de dibujo ----------------
   
    player1 = pygame.draw.rect(screen,WHITE,(paleta1.cord_x,paleta1.cord_y,paleta1.ancho,paleta1.alto))
    player2 = pygame.draw.rect(screen,WHITE,(paleta2.cord_x,paleta2.cord_y,paleta2.ancho,paleta2.alto))
    pelota = pygame.draw.circle(screen,RED,(pelota1.cord_x_pelota,pelota1.cord_y_pelota),16)

    ### ------------ FIN Zona de dibujo -----------

    # Colisiones pelota contra paletas
    if pelota.colliderect(player1) or pelota.colliderect(player2):
        pelota1.speed_x_pelota *= -1

    # Actualizar Pantalla
    pygame.display.flip()
    clock.tick(100)

# €sperar y cerrar el script   
pygame.event.wait(3000)
sys.exit()