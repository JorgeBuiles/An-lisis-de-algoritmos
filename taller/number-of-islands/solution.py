class Solution:
    def numIslands(self, grid):
        filas = len(grid)
        columnas = len(grid[0])
        islas = 0

        def explorar(f, c):
            pila = [(f, c)]
            grid[f][c] = '0'  # se "hunde" al visitarla
            while pila:
                x, y = pila.pop()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < filas and 0 <= ny < columnas and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        pila.append((nx, ny))

        for f in range(filas):
            for c in range(columnas):
                if grid[f][c] == '1':
                    islas += 1
                    explorar(f, c)

        return islas
