import random


def generate_discs(number, radius=0.5, plane=None):
    """generates discs with a given radius on a plane"""
    if plane is None:
        plane = {'min': -15, 'max': 15}
    discs = []
    for i in range(number):
        x = random.uniform(plane['min']+radius, plane['max']-radius)
        y = random.uniform(plane['min']+radius, plane['max']-radius)
        disc = {'r': radius, 'x': x, 'y': y}
        discs.append(disc)
    return discs


def generate_vector(disc, plane):
    """generates random vector, by which a disc can be moved on a plane"""
    xrange = (plane['min']-disc['x'] + disc['r'], plane['max']-disc['x'] - disc['r'])
    yrange = (plane['min']-disc['y'] + disc['r'], plane['max']-disc['y'] - disc['r'])
    x = random.uniform(*xrange)
    y = random.uniform(*yrange)
    return {'x': x, 'y': y}
