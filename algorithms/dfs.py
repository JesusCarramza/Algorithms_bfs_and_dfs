def dfs_algorithm(grid, start, end, rows, cols):
    """
    Generador para DFS.
    Yields (cede): (nodo_actual, conjunto_visitados, diccionario_padres)
    """
    stack = [start] # Pila LIFO
    visited = {start}
    parent = {start: None}

    while stack:
        current = stack.pop() # LIFO: Saca el último que entró

        yield current, visited, parent

        if current == end:
            break

        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        for r, c in neighbors:
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1 and (r, c) not in visited:
                stack.append((r, c))
                visited.add((r, c))
                parent[(r, c)] = current