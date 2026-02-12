import pygame
import sys
from settings import *
from grid_data import GRID_MAP, START_POS, END_POS

def draw_grid(win):
    """Dibuja el mapa completo basado en la matriz GRID_MAP"""
    win.fill(DARK_GREY)

    for row_idx, row in enumerate(GRID_MAP):
        for col_idx, cell in enumerate(row):
            # Calcular la posición (x, y) en píxeles
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE

            # Determinar el color base (Pared o Camino)
            if cell == 1:
                color = GRAY   # Pared
            else:
                color = ORANGE # Camino

            # Sobrescribir color si es Inicio o Fin
            if (row_idx, col_idx) == START_POS:
                color = BLUE
            elif (row_idx, col_idx) == END_POS:
                color = RED

            # Dibujar el rectángulo (celda)
            pygame.draw.rect(win, color, (x, y, TILE_SIZE, TILE_SIZE))
            
            # Dibujar el borde negro para que se vea la cuadrícula
            pygame.draw.rect(win, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)

def main():
    pygame.init()
    # Crear la ventana
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Visualizador BFS & DFS")
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS) # Controlar la velocidad del bucle
        
        # Manejo de eventos (Cerrar la ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibujar todo
        draw_grid(win)
        pygame.display.flip() # Actualizar la pantalla

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()