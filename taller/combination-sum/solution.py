class Solution:
    def combinationSum(self, candidates, target):
        resultado = []
        actual = []

        def backtrack(inicio, resto):
            if resto == 0:
                resultado.append(actual[:])
                return

            for i in range(inicio, len(candidates)):
                if candidates[i] > resto:
                    continue  # poda
                actual.append(candidates[i])         # elegir
                backtrack(i, resto - candidates[i])  # i (no i+1): se puede reutilizar
                actual.pop()                         # deshacer

        backtrack(0, target)
        return resultado
