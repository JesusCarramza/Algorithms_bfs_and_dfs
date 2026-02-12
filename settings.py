# Configuración de la Pantalla
TILE_SIZE = 40  # Tamaño de cada cuadro en píxeles
ROWS = 15
COLS = 15
WIDTH = TILE_SIZE * COLS
HEIGHT = TILE_SIZE * ROWS
FPS = 60        # Fotogramas por segundo del juego

# Colores (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)       # Para las líneas de la cuadrícula
GRAY = (128, 128, 128)  # Para las paredes (Muros)
ORANGE = (255, 165, 0)  # Para el camino libre (suelo)
BLUE = (0, 0, 255)      # Para el nodo INICIO
RED = (255, 0, 0)       # Para el nodo FIN
GREEN = (0, 255, 0)     # Para el camino recorrido / visitado
CYAN = (0, 255, 255)    # Para la frontera (nodos por visitar)
DARK_GREY = (40, 40, 40) # Fondo