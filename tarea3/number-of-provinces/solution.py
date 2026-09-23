class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visitados = [False] * n
        provincias = 0

        def dfs(ciudad):
            visitados[ciudad] = True

            for otra_ciudad in range(n):
                if isConnected[ciudad][otra_ciudad] == 1 and not visitados[otra_ciudad]:
                    dfs(otra_ciudad)

        for ciudad in range(n):
            if not visitados[ciudad]:
                provincias += 1
                dfs(ciudad)

        return provincias

