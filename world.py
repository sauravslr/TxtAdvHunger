_world = {}
the_capitol = (0, 0)


def load_tiles(mapfile, arr, location):
    """Parses a file that describes the world space into the _world object"""
    with open(mapfile, 'r') as f:
        rows = f.readlines()
    # Assumes all rows contain the same number of tabs
    x_max = len(rows[0].split('/'))
    for y in range(len(rows)):
        cols = rows[y].split('/')
        for x in range(x_max):
            # Windows users may need to replace '\r\n'
            tile_name = cols[x].replace('\n', '')
            if tile_name == location:
                global the_capitol
                the_capitol = (x, y)
            arr[(x, y)] = None if tile_name == '' else getattr(
                __import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))
