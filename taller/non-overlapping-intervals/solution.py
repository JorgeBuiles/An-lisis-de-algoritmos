class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Criterio greedy: ordenar por fin y quedarse con el que termina primero
        intervals = self.merge_sort(intervals)

        conservados = 0
        fin_ultimo = float('-inf')

        for inicio, fin in intervals:
            if inicio >= fin_ultimo:
                conservados += 1
                fin_ultimo = fin

        return len(intervals) - conservados

    # Merge sort sobre intervalos, la clave es el extremo derecho (end)
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        medio = len(arr) // 2
        izq = self.merge_sort(arr[:medio])
        der = self.merge_sort(arr[medio:])

        mezcla = []
        i = j = 0
        while i < len(izq) and j < len(der):
            if izq[i][1] <= der[j][1]:
                mezcla.append(izq[i])
                i += 1
            else:
                mezcla.append(der[j])
                j += 1
        mezcla.extend(izq[i:])
        mezcla.extend(der[j:])
        return mezcla
