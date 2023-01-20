import numpy as np
import math
import imi_utils as imi


def world_to_pixel(y:float, x:float, meta_data:dict=None):
    """
    Converts 2D world coordinates (x,y) to continuous(!) pixel coordinates (i,j) given the origin and spacing of an
    image. meta_data is the dictionary of meta_data of the image. It is assumed that the key-words 'origin' and
    'spacing' are defined in the dictionary.
    Note: For 2D numpy-arrays corresponds the last index to the x-coordinate and the  first index to the y-coordinate.
          The numpy array of the image is accessed with input_image[y, x].
          The meta_data is organized the same way, e.g. meta_data['origin'] = (o_y, o_x).

    Argument:
    x,y: 2D world coordiante
    meta_data: a dictionary of meta_data of the image. It is assumed that the key-words 'origin' and
               'spacing' are defined in the dictionary.

    Returns:
    j,i: a 2D tuple with the computed continuous pixel coordinate (float values). Note that the computed values may be
         outside the image space.
    """
    j, i = y, x  # default return identity if no meta_data is given
    if meta_data is not None:
        if not ('origin' in meta_data and 'spacing' in meta_data):
            raise KeyError("ERROR: keywords 'origin' and 'spacing' needed in dictionary meta_data!")
        #compute i, j



    return j, i


def pixel_to_world(j:float, i:float, meta_data:dict=None):
    """
    Converts 2D continuous(!) pixel coordinates (i,j) to world coordinates (x,y) given the origin and spacing of an
    image. meta_data is the dictionary of meta_data of the image. It is assumed that the key-words 'origin' and
    'spacing' are defined in the dictionary.
    Note: For 2D numpy-arrays corresponds the last index to the x-coordinate and the  first index to the y-coordinate.
          The numpy array of the image is accessed with input_image[y, x].
          The meta_data is organized the same way, e.g. meta_data['origin'] = (o_y, o_x).

    Argument:
    i,j: a 2D continuous pixel coordinate (float values).
    meta_data: a dictionary of meta_data of the image. It is assumed that the key-words 'origin' and
               'spacing' are defined in the dictionary.

    Returns:
    y,x: a 2D tuple with the computed world coordinate (float values).
    """
    y, x = j, i  # default return identity if no meta_data is given
    if meta_data is not None:
        if not ('origin' in meta_data and 'spacing' in meta_data):
            raise KeyError("ERROR: keywords 'origin' and 'spacing' needed in dictionary meta_data!")
        # YOUR CODE STARTS HERE -- compute x, y
        # YOUR CODE ENDS HERE
    return y, x


def nearest_neighbour_interp(image:np.ndarray, j:float, i:float):
    """
    Perform nearest neighbor interpolation of an image at continuous(!) pixel coordinate (i,j).  Note that numpy arrays
    are addressed with image[j, i] for coordinate (i,j).

    Argument:
    image: a 2D numpy array representing an gray value image
    i,j: a 2D continuous pixel coordinate (float values).

    Returns:
    value: gray value at continuous pixel position (i,j) in the image computed with nearest neighbor interpolation.
           Returns 0 if (i,j) is outside the image region.
    """
    if i < 0 or i >= image.shape[1] or j < 0 or j >= image.shape[0]:
        return 0
    else:
        return image[round(j), round(i)]



def linear_interp(image:np.ndarray, j:float, i:float):
    """
    Perform linear interpolation of an image at continuous(!) pixel coordinate (i,j). Note that numpy arrays are
    addressed with image[j, i] for coordinate (i,j).

    Argument:
    image: a 2D numpy array representing an gray value image
    i,j: a 2D continuous pixel coordinate (float values).

    Returns:
    value: gray value at continuous pixel position (i,j) in the image computed with linear interpolation.
           Returns 0 if (i,j) is outside the image region.
    """
    # YOUR CODE STARTS HERE
    # YOUR CODE ENDS HERE


def create_image():
    image = np.array([[40,40,220,160], [20,40,160,240], [40,20,180,220], [20,40,220,250]])
    return image


if __name__ == '__main__':
    # Schreiben Sie hier Ihre eigenen Tests für die implementierten Funktionen.
    # Der folgende Code ist als Beispiel gedacht, Sie können das um beliebige Beispiele erweitern

    # simple test image
    img = create_image()
    if False:
        print('Check for nearest neighbour interpolation:')
        continuous_pixel_coords = [(1,1), (1.2, 1.4), (3,0), (2.7, 0.3), (-1.1,2.3), (3,5)]
        for (j, i) in continuous_pixel_coords:
            value = nearest_neighbour_interp(img, j, i)
            print("  image at (i,j)={} is {}".format((i, j), value))
    if False:
        print('Check for linear interpolation:')
        continuous_pixel_coords = [(1, 2), (1.5, 2.7), (1.1, 2.2),(1.2, 0.3), (-1.1, 2.3), (3, 5)]
        for (j, i) in continuous_pixel_coords:
            value = linear_interp(img, j, i)
            print("  image at (i,j)={} = {}".format((i, j), value))
    if False:
        for filename in ['lena.png', 'headMRIT1e.mha', 'ExampleMRISlice.dcm']:
            print('Check for world and pixel coordinates in image {}:'.format(filename))
            img, meta_data = imi.load_image_and_header(filename)
            # print(meta_data)
            print("  Image has origin (y,x)={} and spacing (sy,sx)={}".format(meta_data['origin'], meta_data['spacing']))
            continuous_pixel_coords = [(0, 0), (1, 2), (1.5, 2.7), (1.1, 2.2),(1.2, 0.3), (-1.1, 2.3), (3, 5)]
            for (j, i) in continuous_pixel_coords:
                y, x = pixel_to_world(j, i, meta_data)
                j2, i2 = world_to_pixel(y, x, meta_data)
                print("  Pix-Coord {} -> World Coord {} -> Pix Coord {}". format((i,j), (x,y), (i2,j2)))