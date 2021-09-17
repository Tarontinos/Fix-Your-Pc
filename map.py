from settings import *
#это карта
text_map = [
    '1111111111222244444444444444',
    '1.........2..3....4444444444',
    '1..............44...44444444',
    '1.........2..3..444444444444',
    '1111111111222244444444444444',
]
#------------------------------------------#
world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'
            elif char == '3':
                world_map[(i * TILE, j * TILE)] = '3'
            elif char == '4':
                world_map[(i * TILE, j * TILE)] = '4'
            