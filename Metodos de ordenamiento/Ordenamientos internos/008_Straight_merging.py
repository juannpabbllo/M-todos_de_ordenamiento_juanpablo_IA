"""Straight merging (fusión directa) - implementación mínima.

Este archivo contenía una llamada a `mergesort` que no estaba definida en el
ámbito. Para corregir el error y mantener el cambio pequeño y seguro, incluyo
una implementación local de `mergesort` y `merge` y devuelvo el resultado.
"""

from typing import List


def mergesort(a: List[int]) -> List[int]:
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    resultado: List[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado


def straight_merge(a: List[int]) -> List[int]:
    """Interfaz simple: devuelve la lista ordenada usando merge sort.

    Nota: modifica/retorna una nueva lista (no modifica en sitio).
    """
    return mergesort(a)


if __name__ == "__main__":
    sample = [10, 3, 2, 8, 7, 5]
    print("Antes:", sample)
    sorted_sample = straight_merge(sample)
    print("Después:", sorted_sample)

