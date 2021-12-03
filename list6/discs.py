def is_collision(disc1, disc2):
    """checks if there is a collision between two discs"""
    distance = ((disc1['x'] - disc2['x']) ** 2 + (disc1['y'] - disc2['y']) ** 2) ** 0.5
    if distance < disc1['r'] + disc2['r']:
        return True
    return False


def move(disc, vector):
    """moves disc by a vector"""
    moved_disc = {'r': disc['r'], 'x': disc['x'] + vector['x'], 'y': disc['y'] + vector['y']}
    return moved_disc
