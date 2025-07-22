import pygame

def get_pos_list(arr: list[int], x_center: int, y: int, padding: int, size_x: int) -> list[tuple[int]]:
    n = len(arr)
    pos = []
    total_x = (n * size_x) + ((n-1) * padding)
    left_x = x_center - (total_x/2)
    pos = [(left_x + (i * size_x) + ((i) * padding), y) for i in range(n)]
    return pos
