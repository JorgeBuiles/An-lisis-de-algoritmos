class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Criterio greedy: ordenar por fin y quedarse con el que termina primero
        intervals.sort(key=lambda x: x[1])

        conservados = 0
        fin_ultimo = float('-inf')

        for inicio, fin in intervals:
            if inicio >= fin_ultimo:
                conservados += 1
                fin_ultimo = fin

        return len(intervals) - conservados
