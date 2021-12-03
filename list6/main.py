import matplotlib.pyplot as plt
import remove_collisions as rc
import generator


if __name__ == '__main__':
    plane = {'min': -15, 'max': 15}
    disc_list = generator.generate_discs(100, 0.5, plane)
    figure, axis = plt.subplots(1, 2)
    figure.suptitle('collisions')
    for disc in disc_list:
        uncolored_circle = plt.Circle((disc['x'], disc['y']),
                                      disc['r'],
                                      fill=False)
        axis[0].add_artist(uncolored_circle)
    axis[0].set_title('before')
    axis[0].set_xlim([-15, 15])
    axis[0].set_ylim([-15, 15])
    axis[0].set_aspect(1)

    fixed_list = rc.remove_collisions(disc_list, plane)

    for disc in fixed_list:
        uncolored_circle = plt.Circle((disc['x'], disc['y']),
                                      disc['r'],
                                      fill=False)
        axis[1].add_artist(uncolored_circle)
    axis[1].set_title('after')
    axis[1].set_xlim([-15, 15])
    axis[1].set_ylim([-15, 15])
    axis[1].set_aspect(1)
    plt.show()
