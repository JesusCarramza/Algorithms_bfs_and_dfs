from collections import deque

def bfs_algorithm(grid, start, end, rows, cols):
    """
    Generador para BFS.
    Yields (cede): (nodo_actual, conjunto_visitados, diccionario_padres)
    """
    queue = deque([start])
    visited = {start}
    parent = {start: None} # Para reconstruir el camino final

    while queue:
        current = queue.popleft() # FIFO: Saca el primero que entró

        # En cada paso, le decimos a Pygame: "Estoy aquí, dibújalo"
        yield current, visited, parent

        if current == end:
            break

        row, col = current
        # Vecinos: Arriba, Abajo, Izquierda, Derecha
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        for r, c in neighbors:
            # Verificar límites y paredes (1 es pared)
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1 and (r, c) not in visited:
                queue.append((r, c))
                visited.add((r, c))
                parent[(r, c)] = current