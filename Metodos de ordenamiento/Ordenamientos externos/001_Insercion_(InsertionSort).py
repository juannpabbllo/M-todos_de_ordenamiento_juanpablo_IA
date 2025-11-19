"""Insertion Sort (ordenamiento por inserción) - versíon en Python.

Esta implementación modifica la lista en sitio.
"""

from typing import List


def insertion_sort(a: List[int]) -> None:
    """Ordena la lista `a` en sitio usando insertion sort.

    Args:
        a: lista de enteros a ordenar (se modifica en sitio).
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


if __name__ == "__main__":
    sample = [5, 2, 4, 6, 1, 3]
    print("Antes:", sample)
    insertion_sort(sample)
    print("Después:", sample)
