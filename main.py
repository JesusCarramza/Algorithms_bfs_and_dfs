import pygame
import sys
from settings import *
from grid_data import GRID_MAP, START_POS, END_POS
from algorithms.bfs import bfs_algorithm
from algorithms.dfs import dfs_algorithm

def reconstruct_path(parent, end):
    """Reconstruye el camino desde el final hasta el inicio usando el diccionario de padres"""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent.get(current)
    return path[::-1] # Invertir para que vaya de Inicio a Fin

def draw_grid(win, visited, path_nodes):
    win.fill(DARK_GREY)

    for row_idx, row in enumerate(GRID_MAP):
        for col_idx, cell in enumerate(row):
            x = col_idx * TILE_SIZE
            y = row_idx * TILE_SIZE
            
            # 1. Color base (Pared o Suelo)
            if cell == 1:
                color = GRAY
            else:
                color = ORANGE 

            # 2. Si fue visitado por el algoritmo, píntalo de Cyan claro
            if (row_idx, col_idx) in visited:
                color = CYAN

            # 3. Si es parte del camino final, píntalo Verde
            if (row_idx, col_idx) in path_nodes:
                color = GREEN

            # 4. Inicio y Fin siempre visibles por encima
            if (row_idx, col_idx) == START_POS:
                color = BLUE
            elif (row_idx, col_idx) == END_POS:
                color = RED

            pygame.draw.rect(win, color, (x, y, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(win, BLACK, (x, y, TILE_SIZE, TILE_SIZE), 1)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Presiona 'B' para BFS, 'D' para DFS, 'R' para Reset")
    clock = pygame.time.Clock()

    # Estado del programa
    generator = None      # Aquí guardaremos el algoritmo en ejecución
    visited = set()       # Celdas exploradas
    path_nodes = set()    # El camino final encontrado
    running = True

    while running:
        # Velocidad: Si el algoritmo está corriendo, ve más lento para apreciarlo
        # Si no, ve a 60 FPS para que los inputs reaccionen rápido
        if generator:
            clock.tick(20) # 20 FPS durante la búsqueda
        else:
            clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Controles de Teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and not generator:
                    # Iniciar BFS
                    visited = set()
                    path_nodes = set()
                    generator = bfs_algorithm(GRID_MAP, START_POS, END_POS, ROWS, COLS)
                
                if event.key == pygame.K_d and not generator:
                    # Iniciar DFS
                    visited = set()
                    path_nodes = set()
                    generator = dfs_algorithm(GRID_MAP, START_POS, END_POS, ROWS, COLS)

                if event.key == pygame.K_r:
                    # Reiniciar
                    generator = None
                    visited = set()
                    path_nodes = set()

        # Lógica del Algoritmo (Paso a Paso)
        if generator:
            try:
                # Pedir el siguiente paso al algoritmo
                current_node, current_visited, parents = next(generator)
                visited = current_visited
                
                # Si llegamos al final, reconstruir el camino
                if current_node == END_POS:
                    final_path = reconstruct_path(parents, END_POS)
                    path_nodes = set(final_path)
                    generator = None # Detener el algoritmo
            except StopIteration:
                generator = None # El algoritmo terminó sin encontrar nada (o terminó su ejecución)

        # Dibujar
        draw_grid(win, visited, path_nodes)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()