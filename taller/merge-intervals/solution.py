class Solution:
    def merge(self, intervals):
        intervals = self.merge_sort(intervals)

        resultado = [intervals[0][:]]
        for inicio, fin in intervals[1:]:
            ultimo = resultado[-1]
            if inicio <= ultimo[1]:
                ultimo[1] = max(ultimo[1], fin)
            else:
                resultado.append([inicio, fin])

        return resultado

    # Merge sort sobre intervalos, la clave es el extremo izquierdo (start)
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        medio = len(arr) // 2
        izq = self.merge_sort(arr[:medio])
        der = self.merge_sort(arr[medio:])

        mezcla = []
        i = j = 0
        while i < len(izq) and j < len(der):
            if izq[i][0] <= der[j][0]:
                mezcla.append(izq[i])
                i += 1
            else:
                mezcla.append(der[j])
                j += 1
        mezcla.extend(izq[i:])
        mezcla.extend(der[j:])
        return mezcla
