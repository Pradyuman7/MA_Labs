from numpy import *
from pylab import *
from scipy.ndimage import filters


def compute_harris_response(image, sigma=3):
    temp1 = np.zeros(image.shape)
    filters.gaussian_filter(image, (sigma, sigma), (0, 1), temp1)
    temp2 = np.zeros(image.shape)
    filters.gaussian_filter(image, (sigma, sigma), (1, 0), temp2)

    Wxx = filters.gaussian_filter(temp1 * temp1, sigma)
    Wxy = filters.gaussian_filter(temp1 * temp2, sigma)
    Wyy = filters.gaussian_filter(temp2 * temp2, sigma)
    # determinant and trace
    Wdet = Wxx * Wyy - Wxy ** 2
    Wtr = Wxx + Wyy

    return Wdet / Wtr


def get_harris_points(harrisim, min_dist=10, threshold=0.1):
    """ Return corners from a Harris response image
    min_dist is the minimum number of pixels separating
    corners and image boundary. """
    # find top corner candidates above a threshold
    corner_threshold = harrisim.max() * threshold
    harrisim_t = (harrisim > corner_threshold) * 1
    # get coordinates of candidates
    coords = array(harrisim_t.nonzero()).T
    # ...and their values
    candidate_values = [harrisim[c[0], c[1]] for c in coords]
    # sort candidates
    index = argsort(candidate_values)
    # store allowed point locations in array
    allowed_locations = zeros(harrisim.shape)
    allowed_locations[min_dist:-min_dist, min_dist:-min_dist] = 1
    # select the best points taking min_distance into account
    filtered_coords = []
    for i in index:
        if allowed_locations[coords[i, 0], coords[i, 1]] == 1:
            filtered_coords.append(coords[i])
            allowed_locations[(coords[i, 0] - min_dist):(coords[i, 0] + min_dist),
            (coords[i, 1] - min_dist):(coords[i, 1] + min_dist)] = 0

    return filtered_coords
