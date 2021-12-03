import discs
import generator


def fix_discs(disc_list):
    """creates lists of fixed and not fixed discs"""
    fixed = []
    not_fixed = []
    for disc in disc_list:
        collided = False
        for fixed_disc in fixed:
            if discs.is_collision(disc, fixed_disc):
                collided = True
                break
        if not collided:
            fixed.append(disc)
        else:
            not_fixed.append(disc)
    return fixed, not_fixed


def collision_on_plane(moved_disc, fixed_discs):
    """checks if there are collisions between a given disc and every disc on fixed disc list"""
    for disc in fixed_discs:
        if discs.is_collision(moved_disc, disc):
            return True
    return False


def remove_collisions(disc_list, plane):
    """moves a disc by a random vector, so it is not in collision with any other disc"""
    fixed, not_fixed = fix_discs(disc_list)
    for disc in not_fixed:
        no_collision = False
        while not no_collision:
            vector = generator.generate_vector(disc, plane)
            moved_disc = discs.move(disc, vector)
            if not collision_on_plane(moved_disc, fixed):
                no_collision = True
                fixed.append(moved_disc)
    return fixed
